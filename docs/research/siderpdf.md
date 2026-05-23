PDF Research Report conducted via Sider

PDF extraction research report

Executive finding



Reliable PDF extraction is not solved by picking “the best PDF parser”. It is a pipeline problem.



A PDF is primarily a visual page-description format. It is designed to reproduce pages consistently across systems, not to preserve semantic reading order, key-value relationships, tables, or form intent. The ISO PDF 2.0 standard describes PDF as a digital form for representing electronic documents independently of the environment in which they are created, viewed, or printed; it is aimed at implementers of PDF writers, readers, and processors. That is the root cause of most extraction failures: the text may exist, but its semantic structure may not.



For a production extraction tool, the strongest architecture is:



classify the PDF type;

extract native text with geometry first;

apply table-aware and key-value-aware extraction;

use OCR only where needed;

preserve coordinates, page numbers, parser provenance, and confidence;

validate extracted fields against business rules;

use AI/VLM services selectively for hard layouts rather than as the first-line parser.



For the Collision Engineers document-mapping use case, the most practical baseline is still a deterministic parser-first pipeline: PyMuPDF block/word extraction, pdfplumber or PyMuPDF table detection as a secondary pass, OCR fallback for image-only pages, and optional document-AI/vision-model processing only for difficult scanned or table-heavy documents.



1\. Why PDFs are difficult to extract from

1.1 PDF is visual, not semantic



A PDF page is usually a sequence of drawing commands: place this glyph here, draw this line there, paint this image at these coordinates. A human sees a table, paragraph, or address block. The PDF may only contain absolutely positioned text fragments and vector lines.



The pypdf documentation states the core issue bluntly: PDF files “don’t contain a semantic layer”, and text can be absolutely positioned. It also notes that tables are often just positioned text, and that there may be no unambiguous way to infer paragraphs, headers, footers, tables, ligatures, formulas, or reading order.



This explains common failures:



Failure	Root cause

Text appears in the wrong order	Content stream order is not reading order

Columns are merged together	Text is sorted geometrically without column detection

Table rows become one long line	Cells are just words at coordinates

Header/footer appears mid-document	It may have been inserted later in the content stream

/uni004D/uni0072/... or bad glyphs appear	Font encoding or missing ToUnicode mapping

Missing spaces	PDF may position each glyph manually rather than store word spacing

OCR duplicates native text	A scanned/OCRed hybrid PDF may have both image and text layers

Key-value extraction over-captures	Adjacent table columns appear on the same visual line

1.2 There are several different “PDF types”



A robust parser should classify documents before extraction:



PDF type	Description	Best extraction path

Digitally born PDF	Created from Word, browser, claims portal, reporting software	Native text + geometry

Scanned PDF	Page is an image, no text layer	OCR + layout analysis

OCRed scan	Image plus hidden OCR text layer	Validate OCR layer; possibly re-OCR bad pages

Hybrid PDF	Some pages native, some scanned	Per-page routing

Form PDF	AcroForm/XFA fields, annotations, widgets	Form-field extraction + fallback text

Tagged PDF	Has logical structure tree	Use tags if trustworthy

Encrypted/restricted PDF	May block extraction or require password	Permission handling or rejection

Corrupt/non-standard PDF	Broken xref, malformed streams, odd encodings	Repair/sanitise or fallback parser



The main mistake is treating every PDF as the same problem.



2\. Core extraction techniques

2.1 Native text extraction



Native extraction reads the PDF’s text operators, font encodings, and content streams. It is usually fast and accurate for digitally born PDFs, but unreliable for layout reconstruction.



Typical tools:



PyMuPDF / MuPDF

pdfminer.six

pdfplumber

pypdf

Poppler utilities

PDFBox

iText

PDFium-based tools



Native extraction can output:



plain text;

words with bounding boxes;

lines;

blocks;

spans with font metadata;

characters with coordinates;

images;

vector graphics;

annotations and form fields.



PyMuPDF’s documentation specifically warns that plain text output may not be in natural reading order and may have unexpected line breaks. It recommends using blocks or words when position information matters. PyMuPDF also documents that headers and footers can appear after body text because they may be inserted later, and that sort=True can impose a top-left to bottom-right order.



Best use: digitally born PDFs, claims instructions, invoices, portal-generated reports.



Shortcomings: reading order, tables, multi-column layouts, missing spaces, font encodings, ligatures, rotated text.



2.2 Geometry-aware extraction



Geometry-aware extraction uses bounding boxes rather than plain text. Instead of asking “what text is on the page?”, it asks:



where is each word?

what line is it visually on?

which words are near each other?

what is above, below, left, or right?

which text belongs to the same block?

which label is closest to which value?



This is often the most useful approach for business-document mapping.



A strong geometry pipeline stores each text item like this:



{

&#x20; "text": "Reg No:",

&#x20; "page": 1,

&#x20; "x0": 74.2,

&#x20; "y0": 183.5,

&#x20; "x1": 112.8,

&#x20; "y1": 194.1,

&#x20; "font": "Arial-Bold",

&#x20; "size": 9.0,

&#x20; "parser": "pymupdf"

}



Then it builds higher-level structures:



characters → words;

words → lines;

lines → blocks;

blocks → columns;

labels → values;

table cells → rows.



For a mapping app, this is usually better than trying to reconstruct a perfect text transcript.



Best use: label-value extraction, table cells, addresses, multi-column forms.



Shortcomings: requires coordinate logic; thresholds vary by document; rotated/skewed scanned pages still need OCR/layout correction.



2.3 Table extraction



Tables are one of the hardest parts of PDF parsing because most PDF tables are not stored as table objects. They are typically text fragments plus optional drawn lines.



PyMuPDF’s table documentation notes that a PDF page normally has no embedded table object; tables are usually just styled text, and extraction requires detecting boundaries, borders, and cell text.



There are five main table-extraction strategies.



A. Lattice / ruled-line extraction



This detects drawn horizontal and vertical lines, finds their intersections, builds rectangular cells, then assigns text to cells.



Works well for:



bordered tables;

invoices;

repair estimates;

tabular reports with grid lines.



Fails on:



tables with no borders;

faint or broken lines;

merged cells;

scanned skewed tables;

tables where lines are images, not vector paths.

B. Stream / whitespace extraction



This uses word alignment and whitespace gaps to infer rows and columns.



Works well for:



unruled tables;

simple statements;

monospaced or neatly aligned tables.



Fails on:



irregular spacing;

multi-line cells;

right-aligned numbers;

wrapped descriptions;

dense forms.

C. Hybrid graph extraction



This combines drawn lines, word alignment, cell boundaries, and heuristics. pdfplumber’s approach is a good example: it detects explicit and implied lines, merges overlapping lines, finds intersections, builds cells, then groups contiguous cells into tables.



Works well for:



mixed ruled/unruled tables;

business forms;

semi-structured claims reports.



Fails on:



heavily visual/scanned tables;

unusual merged cells;

tables with images inside cells.

D. Deep-learning table structure recognition



This treats the page or table region as an image and predicts:



table boundaries;

rows;

columns;

cells;

spanning cells;

headers;

table structure as HTML.



PubTables-1M and Table Transformer are important research examples. PubTables-1M contains nearly one million tables with detailed structure annotations and was built partly to solve table over-segmentation and improve table detection, structure recognition, and functional analysis.



Works well for:



complex scientific/financial tables;

scanned tables;

tables with merged cells.



Fails on:



small datasets for niche document types;

domain-specific layouts;

GPU/resource constraints;

occasional structural hallucinations.

E. Vision-language model table extraction



Modern vision-language models can read a table visually and return JSON, HTML, markdown, or schema-specific fields.



Works well for:



complex layouts;

weak visual signals;

forms with non-standard structure;

cases where deterministic parsers fail.



Fails on:



strict auditability;

cost control;

latency;

deterministic repeatability;

hallucination risk;

exact numeric extraction without validation.



The current direction in research is moving toward semantic evaluation rather than purely structural metrics. A 2026 table-parser evaluation paper proposed LLM-as-judge semantic table evaluation and reported stronger correlation with human judgments than traditional TEDS or GriTS metrics.



2.4 OCR-based extraction



OCR is required when the PDF page is just an image. The standard OCR pipeline is:



rasterise page at suitable DPI;

deskew;

denoise;

binarise or enhance contrast;

detect page orientation;

run OCR;

reconstruct words/lines/blocks;

optionally create a searchable PDF text layer;

pass OCR text through the same extraction/mapping pipeline.



OCRmyPDF is a practical open-source tool for this: it adds an OCR text layer to scanned PDFs so they become searchable, while also performing image processing and OCR. Tesseract is the classic open-source OCR engine; current versions include the LSTM OCR engine, support Unicode and over 100 languages, and can output plain text, hOCR, searchable PDF, TSV, ALTO, and PAGE formats.



Best use: image-only PDFs, scanned instructions, legacy documents, screenshots.



Shortcomings: OCR errors, poor handling of small text, tables, stamps, handwriting, skew, reflections, low-resolution scans.



Important rule: do not blindly OCR every PDF. If the document already has a good native text layer, OCR can make extraction worse by introducing recognition errors or duplicate text.



2.5 Tagged PDF, PDF/UA, and PDF/A



A tagged PDF contains a logical structure tree: headings, paragraphs, tables, artifacts, reading order, and sometimes alternative text. This can dramatically improve extraction if the tags are correct.



PDF/UA is the accessibility standard that depends on well-formed tagging. PDF/A variants constrain archival PDFs; some variants require Unicode mappings for text, which can help extraction. However, compliance does not guarantee that business fields are easy to map. A technically compliant PDF can still have awkward layouts, duplicated content, or poor table tagging.



Best use: accessible PDFs, government documents, structured reports.



Shortcomings: many real-world PDFs are untagged; some are incorrectly tagged; many generated business PDFs have weak or absent structure trees.



2.6 Form-field extraction



Some PDFs contain actual form fields:



AcroForm fields;

XFA forms;

checkboxes;

radio buttons;

dropdowns;

annotations;

signatures.



For these, plain text extraction is the wrong first step. The parser should inspect the form field dictionary and annotations. If a field named VehicleReg exists, that is usually more reliable than reading the visual text.



Best use: official forms, claim forms, portal-generated forms.



Shortcomings: XFA support varies; fields may be unnamed or poorly named; visible text and field value can disagree; some forms are flattened and no longer contain fields.



3\. Tooling landscape

3.1 Open-source and local packages

Tool	Main strength	Weakness	Best role

PyMuPDF	Fast native extraction, blocks, words, images, tables, rendering	Requires custom logic for semantic mapping	Primary PDF engine

pdfplumber	Excellent geometry inspection and table debugging	Slower; built on pdfminer; no OCR	Secondary layout/table engine

pdfminer.six	Detailed text/layout parsing	Complex tuning; slower	Deep native text fallback

pypdf	Pure Python, good for manipulation, metadata, page operations	Not OCR; weak layout reconstruction	Fallback, splitting, metadata

Camelot	Table extraction from PDFs	Only certain table styles; requires dependencies	Tabular documents

Tabula	Java-based table extraction	Similar table limitations; Java dependency	Spreadsheet-like PDFs

OCRmyPDF	Adds OCR layer to scanned PDFs	Depends on OCR quality	Preprocess scanned PDFs

Tesseract	Mature OCR engine	Tables/layout need extra processing	Local OCR

PaddleOCR	Strong OCR + table structure models	Heavier dependency; model management	OCR + table/image documents

Unstructured	Partitions documents into semantic elements	Strategy-dependent; can be heavy	General document ingestion

Docling	Converts documents into structured representation	Newer ecosystem; may need tuning	RAG/LLM-ready parsing

Marker	Converts PDFs to markdown/JSON, handles tables/equations/images	GPL licensing; optional LLM mode changes cost/determinism	Markdown/LLM workflows

MinerU	PDF/Office to markdown/JSON, OCR/layout focus	Fast-moving; evaluate carefully	Research/RAG parsing

LayoutParser	Deep-learning document layout analysis toolkit	Requires model selection/training	Custom layout models

PyMuPDF



PyMuPDF is one of the strongest first-line tools for a Windows desktop app because it is fast, local, and gives geometry-rich extraction. It can output text as blocks or words with positional data, which is essential for label-value mapping. It also includes Page.find\_tables(), which attempts to detect and extract tables without requiring external dependencies or cloud AI.



For the CE-style mapping use case, PyMuPDF’s blocks and words modes are more useful than plain text mode because they prevent unrelated columns from being concatenated into one line.



pdfplumber



pdfplumber is valuable when you need to inspect tables and geometry. Its table extraction approach is derived from Nurminen/Tabula-style logic: find explicit and implied lines, merge lines, find intersections, find cells, and group cells into tables. It also exposes debugging tools such as table-finder output and configurable vertical/horizontal strategies.



For production, pdfplumber is a good secondary parser: if PyMuPDF extracts usable text but table layout is ambiguous, run pdfplumber on the relevant pages.



pypdf



pypdf is useful for PDF manipulation, splitting, metadata, encryption handling, and simple extraction. It also provides visitor functions that can ignore header/footer regions based on coordinates. But pypdf’s own documentation stresses that many extraction choices have no single correct answer and that PDF is not designed for parsing.



Use pypdf as a fallback or utility library, not as the primary extractor for complex layouts.



OCRmyPDF and Tesseract



OCRmyPDF is the practical way to convert image-only PDFs into searchable PDFs. Tesseract supplies the OCR engine and can output hOCR, TSV, ALTO, searchable PDF, and other formats.



For a desktop tool, OCR should be optional or fallback-based because it adds time, dependencies, and error risk.



PaddleOCR



PaddleOCR is a more modern OCR/layout/table suite. Its table structure recognition converts table images into editable formats such as HTML, identifying rows, columns, and cells. Its SLANet-family models target table structure recognition, with variants aimed at complex or wireless tables and wired tables.



Use PaddleOCR when scanned tables matter more than lightweight packaging.



Unstructured



Unstructured’s partitioning functions break documents into elements such as titles, narrative text, and list items, and route by file type. It supports multiple formats, including PDFs, and offers strategies such as fast, hi\_res, and ocr\_only; the high-resolution route is used for more accurate layout/table extraction.



This is useful for general ingestion and RAG pipelines, but it may be heavier than needed for a simple deterministic desktop mapper.



Docling



Docling is a newer open-source document parsing toolkit started by IBM Research and hosted under LF AI \& Data. It parses PDFs and other formats, supports advanced PDF understanding including page layout, reading order, table structure, code, formulas, and image classification, and produces a unified DoclingDocument representation.



It is worth testing for markdown/JSON document conversion, especially if future work involves RAG or more complex document understanding.



Marker



Marker converts PDFs and other document formats into markdown/JSON. Its feature list includes table/form/equation formatting, image extraction, header/footer/artifact removal, structured extraction using JSON schemas, and optional LLM-based accuracy improvements.



The main caution is licensing and determinism: Marker is GPL-licensed, and optional LLM mode changes the cost and repeatability profile.



MinerU



MinerU targets complex PDF and Office-document conversion into LLM-ready markdown/JSON, with OCR, layout analysis, table/formula handling, and RAG-oriented output. It is a serious candidate for research or RAG pipelines, but a desktop production tool should benchmark it carefully against speed, packaging burden, and deterministic accuracy.



LayoutParser



LayoutParser is a toolkit for deep-learning-based document image analysis. It provides unified APIs, layout data structures, model support, OCR over detected regions, visualization, and model sharing. It is most relevant when you want to train or apply a custom layout model for document regions.



3.2 Commercial APIs and services

Service	Strength	Weakness	Best use

AWS Textract	Forms, tables, queries, signatures, layout	Cloud cost, privacy, vendor dependency	Forms and scanned business docs

Google Document AI	OCR, form parser, layout parser, custom extractors	Processor setup; cloud dependency	Enterprise extraction workflows

Azure Document Intelligence	Layout, tables, paragraphs, figures, markdown output	Cloud dependency; model-version management	Mixed document extraction

ABBYY Vantage/FlexiCapture	Mature OCR/document capture	Commercial cost, setup complexity	Enterprise OCR/data capture

Rossum/Nanonets/Veryfi/etc.	Invoice/receipt/document workflows	Less control, vendor lock-in	AP/invoice-style extraction

Adobe PDF Extract API	PDF-native structural extraction	Cloud/API dependency	PDF-to-structured-data workflows

AWS Textract



AWS Textract analyzes documents and can return text, forms, tables, query responses, and signatures. It represents forms as key-value pairs and can extract tables, cells, table titles, and footers. It also supports natural-language queries and custom adapters for document-specific extraction.



Best for: cloud workflows where forms/tables matter and the documents are varied.



Main caution: cost, latency, privacy, and cloud dependency.



Google Document AI



Google Document AI transforms unstructured documents into structured data. It supports OCR, layout extraction, key-value pairs, tables, classification, splitting, custom extraction, and pretrained processors.



Best for: enterprise document pipelines, custom processor training, and scalable cloud extraction.



Main caution: setup complexity and cloud dependency.



Azure Document Intelligence



Azure Document Intelligence’s layout model combines OCR and deep learning to extract text, tables, selection marks, and document structure. It supports PDFs, images, and Office formats, and can output pages, paragraphs, lines, words, selection marks, tables, figures, sections, and markdown. It also returns table row/column counts, spans, cell bounding polygons, and column-header indicators.



Best for: structured extraction where layout, tables, figures, and markdown output are useful.



Main caution: cloud dependency and model-version behaviour.



4\. Cutting-edge research directions

4.1 Layout-aware multimodal models



LayoutLMv3 is a major example of multimodal document AI. It uses unified text and image masking plus cross-modal word-patch alignment, and reports strong performance across form understanding, receipt understanding, document VQA, classification, and layout analysis.



The practical implication: modern systems increasingly combine text, layout, and image signals rather than treating OCR text alone as the document.



4.2 OCR-free document understanding



Donut is an OCR-free transformer model for visual document understanding. Its premise is that OCR can be expensive, inflexible, and error-prone; instead, the model reads the document image directly and generates structured output.



This is powerful for certain forms and receipts, but for regulated business workflows it needs careful validation because the model can generate plausible but incorrect text.



4.3 Scientific PDF parsing and markup reconstruction



Nougat targets scientific documents, where formulas and structured markup are difficult to recover from PDFs. It treats scientific document conversion as a visual-to-markup OCR task and focuses on recovering semantic markup from PDF page images.



The lesson generalises: for complex PDFs, especially where layout conveys meaning, “extract text” is too weak. The goal becomes reconstructing semantic structure.



4.4 Better table benchmarks and models



PubTables-1M and Table Transformer advanced table detection and structure-recognition research by providing large-scale table annotations and canonicalized structure.



Newer evaluation work is moving beyond simple structural similarity. For tables, LLM-as-judge semantic evaluation has been proposed because traditional metrics can miss whether the extracted table is meaningfully correct. Formula extraction is seeing similar semantic evaluation work, with LLM-based judging showing stronger correlation with human assessment than conventional text-similarity metrics.



4.5 Large document-parsing benchmarks



OmniDocBench is a benchmark for diverse PDF parsing with multiple document types, layout categories, and attribute labels, designed to compare modular pipelines and end-to-end multimodal approaches. Real5-OmniDocBench extends this idea by testing robustness under real-world physical distortions such as scanning, warping, screen photography, illumination changes, and skew.



This matters because many business PDFs are not clean academic PDFs. They are screenshots, scans, phone photos, portal exports, or OCRed documents.



4.6 Vision-language parsing systems



MonkeyOCR proposes a structure-recognition-relation paradigm for document parsing: identify where elements are, what they are, and how they are organised. It reports improvements over MinerU on average performance, table extraction, and formula recognition. MonkeyOCR v1.5 further uses a two-stage process: predict layout and reading order first, then recognise localized content, with additional reinforcement-style optimisation for table rendering.



PaddleOCR-VL is another recent vision-language model direction, combining dynamic-resolution visual encoding with language modelling and targeting multilingual documents, tables, formulas, and charts.



The trend is clear: the frontier is shifting from “OCR text then parse” to “understand the page as a multimodal object”.



5\. Industry-standard extraction architecture



A serious extraction system should be built as a cascade, not a single parser.



5.1 Recommended pipeline

Step 1 — File intake and safety

verify file type;

reject unsupported/encrypted files unless credentials are available;

impose page/file-size/time limits;

sandbox parsing where possible;

avoid executing embedded scripts or actions;

normalise corrupt PDFs where feasible.

Step 2 — Document classification



Classify per document and per page:



native text present?

text density?

image coverage?

OCR layer present?

form fields present?

table-like geometry?

rotated pages?

page size anomalies?

scanned/photographed page?



This controls the extraction route.



Step 3 — Native extraction



Run a native parser first:



PyMuPDF blocks;

PyMuPDF words;

optionally pdfplumber words/chars;

form fields and annotations;

images and vector lines.



Keep structured geometry, not just plain text.



Step 4 — Layout reconstruction



Build:



lines;

blocks;

columns;

reading-order groups;

page regions;

label-value candidates;

table candidates.



For user-configured mapping, store both:



a human-readable preview;

a structured internal representation.

Step 5 — Table pass



Use one or more:



PyMuPDF find\_tables;

pdfplumber table finder;

Camelot/Tabula for specific table-heavy PDFs;

OCR/table model for scanned tables.



Do not assume table extraction should overwrite the text transcript. It should provide an additional structured representation.



Step 6 — OCR fallback



Use OCR when:



no native text exists;

text layer is obviously bad;

page is mostly image;

key fields are missing and visual text exists.



Prefer per-page OCR rather than whole-document OCR.



Step 7 — Field extraction



Field extraction should be separate from PDF extraction.



Possible strategies:



literal label matching;

regex matching;

coordinate-based label-to-right / label-to-below;

table cell lookup;

form-field lookup;

fallback OCR lookup;

optional AI schema extraction.



Each extracted field should carry:



{

&#x20; "value": "AB12CDE",

&#x20; "field": "VRM",

&#x20; "source\_page": 1,

&#x20; "source\_text": "Reg No: AB12 CDE",

&#x20; "bbox": \[72.1, 183.5, 133.9, 194.2],

&#x20; "method": "label\_right\_geometry",

&#x20; "parser": "pymupdf\_words",

&#x20; "confidence": 0.93

}

Step 8 — Validation and normalisation



Business validation is critical:



VRM format;

date format;

mileage numeric cleanup;

mileage unit accepted values;

VAT status accepted values;

postcode normalisation;

reference format;

mandatory provider/work-provider check.



This is where domain logic belongs.



Step 9 — Human review



For a desktop mapping tool, the UI should show:



detected values;

source text preview;

highlighted source spans;

parser warnings;

missing mandatory fields;

replaced/overwritten fields;

export blockers.



The goal is controlled automation, not invisible automation.



6\. Technique comparison

Technique	Accuracy on clean digital PDFs	Accuracy on scans	Tables	Speed	Determinism	Auditability

Plain native text	Medium	None	Poor	Very high	High	Medium

Blocks/words with geometry	High	None	Medium	High	High	High

pdfplumber-style table detection	High on suitable PDFs	None	High for ruled/aligned tables	Medium	High	High

OCR/Tesseract	None/low need	Medium	Poor-medium	Medium-low	Medium	Medium

PaddleOCR/table models	Medium	High	High	Medium-low	Medium	Medium

Cloud Document AI	High	High	High	Medium	Medium	Medium-high

Vision-language models	Medium-high	High	High	Low-medium	Lower	Lower unless constrained

Manual mapping with validation	High when configured	Depends on upstream OCR	Depends	High	High	High



The practical conclusion: deterministic native extraction plus geometry should be the default. OCR and AI should be targeted fallbacks.



7\. Common implementation traps

7.1 Treating “text extraction” as enough



Plain text extraction is not enough for forms and tables. It loses the spatial relationships that make business documents understandable.



7.2 Sorting everything top-left to bottom-right



Top-left sorting helps, but it can break multi-column documents. It may combine unrelated cells on the same y-coordinate or put sidebars into the body text.



7.3 Overusing OCR



OCR can degrade high-quality digital PDFs. It can introduce wrong characters, duplicate text, and poor spacing.



7.4 Ignoring font encodings



Bad or missing ToUnicode maps can produce garbage text. A good pipeline should detect suspicious extracted text and fall back to another parser or OCR.



7.5 Assuming table extraction is universal



A parser that works on ruled invoices may fail on unruled schedules. A table extractor should be selected by table type.



7.6 Letting AI output bypass validation



LLM/VLM extraction can be useful, but every field should still pass deterministic validation. For claim and vehicle data, schema validation is mandatory.



7.7 Not storing provenance



Without source page, bounding box, parser method, and source text, debugging extraction failures becomes guesswork.



8\. Recommendations for a CE-style document mapper

8.1 Best immediate stack



For a lightweight Windows desktop app:



Primary PDF parser: PyMuPDF.

Primary extraction mode: blocks and words, not plain text.

Table secondary pass: PyMuPDF find\_tables and/or pdfplumber for table-heavy PDFs.

Fallback parser: pypdf for basic text and metadata fallback.

OCR fallback: OCRmyPDF/Tesseract for image-only PDFs.

Optional advanced parser: Docling, Marker, MinerU, or PaddleOCR for research/testing, not necessarily first production integration.



This keeps the application deterministic, local, and relatively easy to package.



8.2 Suggested internal representation



Do not store only one string. Store three layers:



Layer 1: Raw extracted text preview

Layer 2: Structured geometry objects

Layer 3: Field extraction results



Example:



{

&#x20; "pages": \[

&#x20;   {

&#x20;     "page": 1,

&#x20;     "blocks": \[],

&#x20;     "words": \[],

&#x20;     "tables": \[],

&#x20;     "images": \[]

&#x20;   }

&#x20; ],

&#x20; "fields": {

&#x20;   "VRM": {

&#x20;     "value": "AB12CDE",

&#x20;     "source": "Reg No: AB12 CDE",

&#x20;     "page": 1,

&#x20;     "bbox": \[100, 200, 160, 214],

&#x20;     "method": "single\_label",

&#x20;     "parser": "pymupdf\_blocks"

&#x20;   }

&#x20; }

}



This lets the UI show normal text while the extraction engine uses geometry.



8.3 Mapping methods worth supporting



Current user-configured mapping methods are sensible, but the next level would be geometry-aware variants:



Method	Description

Single label	Find label, extract text after it

Two labels	Extract between labels

Fixed position	Extract by line/position

Manual input	User-supplied

Label-right	Find label and nearest text to the right

Label-below	Find label and nearest text below

Table cell	Find row label and column label intersection

Presence check	Token present → controlled value

Regex capture	User-supplied capture group

Page-region rule	Only search in a defined page area



The important point is that user-configured rules should be explicit. Hidden fallback logic can create surprising results.



8.4 Table handling for vehicle/insurance documents



For reports like engineer reports, invoices, and assessment PDFs, tables should be handled in two ways:



Preview text mode: keep blocks separated so label-value pairs do not contaminate each other.

Structured table mode: detect tables separately and expose cells internally.



A table like:



Reg No: AB12CDE    Registered: 2020    Type: Estate



should not be treated as one extractable line for the Reg No field. It should become separate block/cell candidates:



\[

&#x20; {"label": "Reg No", "value": "AB12CDE"},

&#x20; {"label": "Registered", "value": "2020"},

&#x20; {"label": "Type", "value": "Estate"}

]



That directly prevents over-capture.



8.5 OCR policy



A practical OCR decision rule:



If native text length per page is meaningful:

&#x20;   use native extraction

else if page image coverage is high:

&#x20;   OCR that page

else:

&#x20;   mark page as extraction-risk



Then only OCR pages that need it.



9\. Evaluation framework



A PDF extraction system should be evaluated at the field level, not only at text level.



9.1 Build a gold set



Create a test library with:



clean digital PDF;

table-heavy PDF;

scanned PDF;

OCRed scan;

poor OCR;

multi-column report;

PDF with headers/footers;

PDF with images only;

PDF with hidden text layer;

PDF with bad font encoding;

PDF with rotated pages;

PDF with form fields;

PDF with missing work provider;

PDF containing only images.



For each document, define expected output:



{

&#x20; "Work Provider": "SBL",

&#x20; "VRM": "AB12CDE",

&#x20; "Vehicle Model": "BMW 320D",

&#x20; "Reference": "ABC123",

&#x20; "Incident Date": "01/02/2026"

}

9.2 Metrics



Use:



Metric	Purpose

Field exact match	Main business metric

Normalised field match	Handles spacing/case/date normalisation

False positive rate	Prevents UnknownVRM-style exports

Missing mandatory field rate	Export safety

Table cell accuracy	Table extraction quality

OCR character error rate	OCR quality

Processing time	UX/desktop feasibility

Parser fallback rate	Pipeline health

Manual correction rate	Real-world usefulness



For table extraction research, newer semantic metrics may be more meaningful than pure cell-structure metrics, especially when the downstream task is data extraction rather than visual reconstruction.



10\. Practical decision matrix

Use case	Recommended method

Clean generated instruction PDF	PyMuPDF blocks/words

PDF with simple labels	Single-label or geometry label-right

Multi-column PDF	Blocks/words with column detection

Bordered table	PyMuPDF find\_tables or pdfplumber lattice logic

Unbordered table	pdfplumber stream logic or geometry clustering

Scanned PDF	OCRmyPDF/Tesseract or PaddleOCR

Scanned table	PaddleOCR table model or cloud Document AI

Complex form	Azure/Google/AWS Document AI or custom model

Scientific PDF/equations	Nougat/Marker/MinerU-style parser

RAG markdown conversion	Docling, Marker, MinerU, Unstructured

Strict deterministic desktop app	PyMuPDF + pdfplumber + OCR fallback

Highest automation over varied docs	Cloud Document AI + validation layer

11\. Key conclusions

PDF extraction is inherently lossy unless the PDF contains reliable structure. The format preserves visual appearance, not necessarily meaning.

Native text extraction should be first, but not plain-text-only. Use words, blocks, coordinates, fonts, and page regions.

Tables need separate handling. A table is not just text with line breaks. Use table detectors, geometry, and cell assignment.

OCR is a fallback, not a default. It is essential for scans but can damage clean digital extraction.

Vision-language models are promising but should be constrained. They are useful for difficult documents, but outputs need schema validation and provenance.

The most robust production architecture is a cascade. Parser-first, geometry-aware, OCR fallback, AI optional, validation mandatory.

For CE Document Mapper specifically, the correct direction is deterministic extraction plus user-controlled mapping. PyMuPDF block/word extraction, table-aware fallbacks, OCR for image-only PDFs, and strict export validation are the right foundation.

Thought for 4m 23s

PDF extraction, parsing, OCR, and document-AI research report

Executive conclusion



PDF extraction should be treated as a document-understanding pipeline, not as a single parser choice. A PDF is fundamentally a visual document representation. ISO 32000-2 describes PDF as a digital form for representing electronic documents so they can be exchanged and viewed independently of the creation/viewing/printing environment; it is aimed at PDF writers, readers, interactive processors, and other PDF processors. That design goal explains the core extraction problem: a PDF can display a table, address block, or invoice perfectly while storing little or no reliable semantic information about rows, cells, labels, reading order, or fields.



The most reliable production approach is:



Classify each PDF: digital, scanned, OCRed scan, hybrid, form, tagged, encrypted, corrupt.

Extract native text first, preserving page, block, word, coordinates, font metadata, and parser provenance.

Use geometry-aware mapping for label-value fields.

Use table-specific extraction separately from plain text extraction.

OCR only the pages that need OCR.

Use cloud Document AI or vision-language models only where deterministic extraction fails or where varied scanned layouts justify the cost.

Validate every output field against business rules before export.



For a lightweight Windows desktop app such as CE Document Mapper, the strongest baseline remains: PyMuPDF blocks/words first, pdfplumber table fallback, OCRmyPDF/Tesseract for scanned pages, and optional Docling/Marker/MinerU/PaddleOCR for research or difficult documents.



1\. Why PDF extraction is hard

1.1 Missing semantic layer



The central issue is that most PDFs do not store “this is a paragraph”, “this is a table”, “this is a value for this label”, or “this is the correct reading order”. The pypdf documentation states that PDF was created to produce the desired visual result for printing and was not created for content parsing. It specifically notes that PDFs do not contain a semantic layer and that headers, footers, tables, paragraphs, and page numbers are not inherently identified.



This is why plain text extraction often fails on documents that look simple to a human. A row such as:



Reg No: AB12CDE        Registered: 2020        Type: Estate



may be stored as separate positioned glyphs, or as fragments in an order that has little relationship to how the eye reads the page. pypdf also notes that tables are typically absolutely positioned text and, in the worst case, every single letter can be absolutely positioned, making columns and rows difficult to infer.



1.2 Reading order is not guaranteed



PyMuPDF’s documentation makes the same point from a practical extraction perspective: plain text output from a PDF may not be in normal reading order and may contain unexpected line breaks. It recommends extracting blocks or words with positional information when reading order or location matters.



Headers and footers are a common example. A PDF creator can insert header/footer text after the main body content, so a text extractor may output the body first and the header/footer later. PyMuPDF recommends sorting text top-left to bottom-right or using layout-preserving approaches to re-establish reading sequence.



1.3 PDF type matters



The extraction route should vary by PDF type. pypdf distinguishes digitally born PDFs, scanned PDFs, and OCRed PDFs: digitally born PDFs contain text objects; scanned PDFs are essentially image containers; OCRed PDFs often contain an image with OCR text hidden behind it.



A practical classifier should separate:



PDF type	Extraction strategy

Digitally born PDF	Native parser first: blocks, words, spans, coordinates

Scanned PDF	OCR + layout analysis

OCRed scan	Validate hidden OCR layer; re-OCR poor pages if needed

Hybrid PDF	Route per page

Form PDF	Extract AcroForm/XFA/annotations first

Tagged PDF	Use tag structure if reliable

Table-heavy PDF	Run table detector separately

Copy-protected/encrypted PDF	Permission handling or image/layout fallback

Corrupt PDF	Repair/sanitise or parser fallback

2\. Core extraction techniques

2.1 Native text extraction



Native text extraction reads PDF text operators, font encodings, content streams, and positioning instructions. It is fast and usually best for digitally born PDFs.



Typical native parsers:



Tool	Role

PyMuPDF / MuPDF	Fast extraction, words, blocks, spans, images, rendering, table detection

pdfminer.six	Detailed layout/text analysis

pdfplumber	Geometry-heavy wrapper around pdfminer; very useful for tables and debugging

pypdf	Pure Python PDF manipulation and basic extraction

PDFBox	Java PDF parsing/manipulation

Poppler utilities	Mature command-line extraction/rendering

iText	Commercial/open-source PDF SDK depending on use case and license

PDFium-based libraries	Rendering and low-level PDF handling



Strength: fast, deterministic, local, no OCR errors.

Weakness: layout reconstruction is not guaranteed.

Best use: clean generated PDFs, claim instructions, invoices, portal reports.



For the CE use case, PyMuPDF blocks and words are more valuable than plain text, because they preserve coordinates and reduce the risk of adjacent columns contaminating extracted values. PyMuPDF explicitly supports extracting text as blocks and words with position information.



2.2 Geometry-aware extraction



Geometry-aware extraction treats the PDF page as a coordinate system. Each word, span, or block is stored with:



{

&#x20; "text": "Reg No:",

&#x20; "page": 1,

&#x20; "x0": 72.4,

&#x20; "y0": 180.2,

&#x20; "x1": 112.9,

&#x20; "y1": 193.8,

&#x20; "parser": "pymupdf",

&#x20; "font": "Arial-Bold",

&#x20; "size": 9.0

}



Then higher-level logic reconstructs:



words into lines;

lines into blocks;

blocks into columns;

labels into values;

table cells into rows/columns;

page regions into named areas.



This is the right model for form-like insurance and vehicle documents. It supports rules like “label-right”, “label-below”, “nearest value after label”, “same row”, and “same table cell”.



2.3 Table extraction



Tables are one of the hardest PDF extraction problems because they are usually not stored as table objects. PyMuPDF notes that a visible table is normally just standard text formatted as tabular data, and extraction requires identifying the table area, column borders, and relevant text positions.



There are four main approaches.



Lattice / ruled-line extraction



This detects vector lines, intersections, rectangles, and cell boundaries.



Works well for: invoices, bordered estimates, spreadsheets exported to PDF.

Fails on: tables without borders, broken/faint rules, merged cells, image-only scans.



Stream / whitespace extraction



This infers columns and rows from aligned words and whitespace gaps.



Works well for: unruled but well-aligned tables.

Fails on: dense text, wrapped cells, irregular spacing, right-aligned numbers.



Hybrid geometric extraction



pdfplumber’s table detection is a strong example. It finds explicit lines and implied lines from word alignment, merges nearly overlapping lines, finds intersections, derives rectangular cells, then groups contiguous cells into tables. It also exposes extract\_table, extract\_tables, find\_table, and debug\_tablefinder, with configurable vertical/horizontal strategies and tolerances.



Works well for: business documents where tables are mostly geometric.

Fails on: heavily scanned/warped pages, handwritten tables, very complex merged cells.



ML / vision table extraction



Modern systems detect tables and cells from the rendered page image. PaddleOCR’s table structure recognition module converts non-editable table images into editable formats such as HTML and identifies row, column, and cell positions. PaddleOCR’s SLANet/SLANet\_plus/SLANeXt models are specifically aimed at table structure recognition, with variants for complex, wireless, and wired tables.



Works well for: scanned tables, visual tables, complex structures.

Fails on: packaging complexity, GPU requirements, domain mismatch, occasional structural errors.



2.4 OCR



OCR is necessary when the PDF page is an image. OCRmyPDF adds an OCR text layer to scanned PDFs so they become searchable, and it applies image processing and OCR to existing PDFs.



Tesseract remains the main open-source OCR engine. It includes an LSTM-based OCR engine, supports Unicode, recognizes more than 100 languages, supports image formats such as PNG/JPEG/TIFF, and can output plain text, hOCR, searchable PDF, invisible-text-only PDF, TSV, ALTO, and PAGE.



OCR should not be applied blindly to every PDF. pypdf explicitly advises against always OCRing digitally born PDFs because native extraction can use information from the PDF itself, including fonts, encodings, and character-distance information, whereas OCR may confuse visually similar characters.



Best use: image-only PDFs, scans, screenshots, poor native text layer.

Weakness: character errors, table structure loss, latency, dependency burden, duplicated OCR/native text.



2.5 Tagged PDF and PDF/UA



Tagged PDF is the closest thing PDFs have to a semantic layer. PDF/UA depends on semantic information describing logical structure such as sections, paragraphs, lists, and tables; the PDF feature that represents this semantic information is “Tagged PDF”.



In theory, tagged PDFs can provide better reading order and structure. In practice, many business PDFs are untagged or poorly tagged. PDF/UA conformity also does not necessarily guarantee the content itself is accessible or easy to extract; PDF/UA states technical features, not the full conversion process or every accessibility outcome.



2.6 Form-field extraction



Some PDFs contain AcroForm fields, checkboxes, radio buttons, annotations, or signatures. In those cases, the form data should be extracted directly before trying to infer fields visually. pdfplumber’s documentation includes an AcroForm field traversal example and shows extracted form tuples containing field names, alternate names, and values.



Best use: official forms, structured claim forms, editable PDF forms.

Weakness: fields may be flattened, poorly named, duplicated, or inconsistent with visible text.



3\. Tool and service landscape

3.1 Open-source / local tools

Tool	Strength	Shortcoming	Best role

PyMuPDF	Very fast; blocks, words, spans, rendering, images, table finder	Requires custom semantic logic	Primary parser for digital PDFs

pdfplumber	Strong geometry/table inspection; configurable table extraction	Slower; no OCR by itself	Secondary table/layout parser

pdfminer.six	Detailed text/layout internals	Tuning can be complex	Fallback and detailed layout work

pypdf	Pure Python; manipulation, splitting, metadata, visitor hooks	Not OCR; weak for layout	Utility/fallback

OCRmyPDF	Converts scanned PDFs into searchable PDFs	Dependent on OCR quality	Scan preprocessing

Tesseract	Mature OCR, many output formats	Needs image preprocessing; weak tables by itself	Local OCR backend

PaddleOCR	OCR + table/layout models	Heavier dependency/model stack	Scanned or table-heavy docs

Unstructured	Generic partitioning into document elements	Strategy-dependent; heavier	RAG/general ingestion

Docling	Modern PDF/Office parsing for gen-AI pipelines	Newer ecosystem; needs benchmarking	Markdown/JSON/RAG parsing

Marker	Converts documents to Markdown/JSON/HTML/chunks; tables/forms/equations; optional LLM mode	GPL/commercial considerations; LLM mode affects determinism/cost	LLM-ready extraction

MinerU	Complex PDF/Office/image parsing to Markdown/JSON; OCR, formulas, tables, layouts	Hardware/storage/dependency load	High-end document parsing/RAG

LayoutParser	Deep-learning layout detection toolkit	Needs model selection/training	Custom layout models



Unstructured supports multiple file formats and provides PDF strategies including auto, hi\_res, ocr\_only, and fast. Its docs say fast uses pdfminer when text is extractable, ocr\_only uses Tesseract, and hi\_res uses a document-layout model, with table extraction for PDFs requiring hi\_res in certain configurations.



Docling positions itself as a document-processing toolkit for gen-AI use cases. It supports multiple formats, advanced PDF understanding including page layout, reading order, table structure, formulas, and image classification, plus OCR support and a unified DoclingDocument representation.



Marker converts documents to Markdown, JSON, chunks, and HTML. Its README lists support for PDFs, images, Office files, HTML, EPUB, multilingual documents, tables, forms, equations, image extraction, header/footer removal, JSON-schema-based structured extraction, and optional LLM accuracy boosting. It also exposes options for JSON/Markdown/HTML/chunk output, forced OCR, stripping existing OCR, and LLM mode.



MinerU is a high-end open-source parser for LLM/RAG workflows. Its README says it converts PDFs, Office files, images, and web pages into structured Markdown/JSON, uses VLM+OCR, supports 109 languages, handles formulas, tables, scanned docs, handwriting, multi-column layouts, cross-page tables, and automatic header/footer removal. It also warns that document parsing remains difficult for complex layouts, scanned pages, and handwritten content, which is a useful caution for production use.



LayoutParser is useful when you want a custom deep-learning layout workflow. It provides deep-learning layout detection models, layout data structures, region filtering, OCR over detected regions, visualization, and layout loading from JSON/CSV/PDF.



3.2 Commercial/cloud services

Service	Strength	Shortcoming	Best role

AWS Textract	Text, forms, tables, queries, signatures, layout	Cloud cost/privacy; adapter setup	Varied forms/tables

Google Document AI	OCR, layout, KVP, tables, classification, custom extractors	Cloud setup; processor selection	Enterprise workflows

Azure Document Intelligence	OCR + deep learning layout; tables, figures, paragraphs, selection marks, markdown	Cloud dependency; quotas/model versions	General cloud extraction

Adobe PDF Extract API	Native/scanned PDF structural extraction; JSON/Markdown; tables/figures	Cloud dependency	PDF-to-structure/LLM workflows

ABBYY Vantage/FlexiCapture	Mature enterprise OCR/document capture	Commercial setup/cost	High-volume capture

Rossum/Nanonets/Veryfi/etc.	Business-document workflows	Vendor lock-in; less control	Invoice/receipt/AP workflows



AWS Textract analyzes documents for text, forms, tables, query responses, and signatures. It represents forms as key-value pairs, extracts table cells/titles/footers, supports natural-language queries, and can use custom adapters trained on labelled documents.



Google Document AI is a document processing and understanding platform that transforms unstructured documents into structured data. It supports OCR, text/layout extraction, entity normalization, key-value pairs, regular tables, classification, splitting, custom extractors, pretrained processors, and integration with storage/search/data systems.



Azure Document Intelligence’s layout model combines OCR with deep learning to extract text, tables, selection marks, and document structure. It supports PDFs, image files, and Office formats, and returns structured elements such as pages, paragraphs, lines/words, selection marks, tables, figures, sections, and markdown output.



Adobe PDF Extract API is a cloud service that extracts content and structural information from native or scanned PDFs. It can output structured JSON or Markdown, extract text in contextual blocks, parse complex tables including row/column-spanning cells, and output table data as JSON, CSV, XLSX, and table PNGs for validation.



4\. Cutting-edge research directions

4.1 Layout-aware multimodal transformers



LayoutLMv3 is a major layout-aware Document AI model. It uses unified text and image masking plus word-patch alignment, and reports strong performance across form understanding, receipt understanding, document VQA, document classification, and layout analysis.



The lesson is that modern document extraction is no longer just OCR text plus regex. Competitive systems combine:



text;

visual image patches;

bounding boxes;

reading order;

page structure;

cross-modal alignment.

4.2 OCR-free document understanding



Donut is an OCR-free Document Understanding Transformer. The paper argues that OCR-based visual document understanding suffers from OCR cost, inflexibility, and error propagation, then proposes a transformer that reads document images directly and generates structured output.



This is powerful for certain receipts/forms, but production use needs strict validation. OCR-free models can produce clean-looking structured output that is still wrong.



4.3 Scientific PDF reconstruction



Nougat targets scientific documents and argues that PDFs cause loss of semantic information, especially for mathematical expressions. It uses a visual transformer to convert scientific document images into markup language.



This is relevant beyond academia: for any complex PDF, the goal may not be “extract text”; it may be “reconstruct semantic markup”.



4.4 Table-specific datasets and models



PubTables-1M is an important table extraction dataset. It contains nearly one million tables from scientific articles, supports multiple input modalities, includes detailed header and location information, and addresses over-segmentation through canonicalization. Transformer-based object-detection models trained on it performed well for table detection, structure recognition, and functional analysis.



The broader trend is that table extraction is moving from rule-based cell inference toward object detection, graph modelling, and vision-language structure reconstruction.



4.5 Benchmarks for real document parsing



OmniDocBench was introduced to evaluate diverse PDF document parsing across multiple document types with 19 layout category labels and 14 attribute labels. It compares modular pipelines and multimodal end-to-end methods, highlighting limitations in diversity and evaluation fairness.



This matters because a parser that performs well on clean academic PDFs may fail on invoices, scanned forms, screenshots, multi-column reports, or engineer assessments.



4.6 Vision-language document parsers



MonkeyOCR proposes a structure-recognition-relation triplet: “Where is it?”, “What is it?”, and “How is it organized?”. The paper reports that this decomposition improves document parsing efficiency and accuracy, outperforming MinerU on average in its experiments and showing particular gains on formulas and tables.



PaddleOCR-VL is another recent direction: a compact 0.9B vision-language model for multilingual document parsing, using a dynamic-resolution visual encoder and a language model to recognize text, tables, formulas, and charts across 109 languages.



The frontier is therefore moving toward VLM-assisted parsing, but deterministic extraction still matters for auditability, cost, and exact-field workflows.



5\. Industry-standard production architecture



A robust PDF extraction system should be a cascade.



5.1 Intake and safety



At import:



verify MIME/type;

cap file size and page count;

detect encryption/password protection;

sandbox risky parsing where possible;

avoid executing embedded scripts/actions;

record parse errors per file/page.

5.2 Per-document and per-page classification



Classify:



native text density;

image coverage;

OCR layer presence;

form fields;

table-like geometry;

rotated/skewed pages;

page size anomalies;

scanned/photographed content;

suspicious text encoding.



This prevents expensive OCR or VLM parsing being applied unnecessarily.



5.3 Native parser pass



Run a native parser first for digital PDFs:



PyMuPDF blocks;

PyMuPDF words;

optionally PyMuPDF dict/rawdict;

form fields and annotations;

images;

vector lines/rectangles;

page dimensions and rotation.



Store the geometry. Do not reduce the document to a single string too early.



5.4 Layout reconstruction



Build:



lines;

blocks;

columns;

page regions;

label-value candidates;

table candidates;

reading-order groups.



For field mapping, keep text and geometry together.



5.5 Table extraction pass



Run table extraction separately:



PyMuPDF find\_tables() where it works;

pdfplumber table finder for configurable geometric tables;

Camelot/Tabula for classic lattice/stream cases;

PaddleOCR or cloud layout tools for scanned/complex tables.



The table output should not replace the text output. It should become another structured layer.



5.6 OCR fallback



Only OCR when:



native text is missing;

text density is too low;

the page is mostly image;

the hidden OCR layer is poor;

required fields are missing but visual text exists.



OCR should be per-page where possible, not necessarily whole-document.



5.7 Field extraction



Field extraction should be a separate layer from PDF parsing.



Recommended methods:



Method	Use

Single label	“Reg No:” → value after label

Two labels	Extract between start/end labels

Fixed position	Stable line/page templates

Label-right	Nearest text to the right

Label-below	Nearest text below

Table cell	Row/column intersection

Regex capture	Format-constrained values

Page-region rule	Search only in a defined area

Presence check	Yes/No or Miles/Km style fields

Manual input	Controlled fallback



Each extracted value should carry provenance:



{

&#x20; "field": "VRM",

&#x20; "value": "AB12CDE",

&#x20; "page": 1,

&#x20; "bbox": \[74.2, 183.5, 142.1, 194.0],

&#x20; "source\_text": "Reg No: AB12 CDE",

&#x20; "method": "label\_right\_geometry",

&#x20; "parser": "pymupdf\_words",

&#x20; "confidence": 0.94

}

5.8 Validation



Validation should be deterministic and field-specific:



VRM cleanup and format checks;

mileage numeric cleanup;

mileage unit constrained to known values;

VAT status constrained to known values;

date normalization;

postcode normalization;

required work-provider check;

export blocking for unidentified documents.



This is especially important where an image-only PDF or unrelated document could otherwise create an UnknownVRM.json-style file.



6\. Strengths and shortcomings by approach

Approach	Strengths	Shortcomings	Best use

Plain native text	Fast, simple	Bad reading order; tables contaminated	Quick preview

Blocks/words with geometry	Fast, auditable, strong for labels	Requires custom logic	Business-field mapping

pdfplumber table extraction	Transparent, configurable	Sensitive to thresholds/layout	Tables in digital PDFs

OCRmyPDF/Tesseract	Local scan support	OCR errors, preprocessing needed	Image-only PDFs

PaddleOCR/table models	Strong visual table support	Heavier stack	Scanned/complex tables

Unstructured	Broad document ingestion	Strategy/dependency complexity	RAG pipelines

Docling	Rich gen-AI parsing	Needs benchmarking	Markdown/JSON/RAG

Marker	Strong document-to-markdown/JSON, optional LLM mode	License/commercial/LLM implications	LLM-friendly extraction

MinerU	High-end complex parsing	Resource/dependency burden	Large-scale document parsing

Cloud Document AI	Strong forms/tables/layout	Cost, privacy, vendor dependency	Enterprise automation

VLM/LLM parsing	Handles hard visual cases	Hallucination, cost, audit risk	Fallback, not first-line

7\. Specific recommendations for CE Document Mapper

7.1 Best local-first stack



For the current app style—lightweight Windows desktop, simple UI, provider presets, deterministic mapping—the best stack is:



PyMuPDF as primary PDF parser. Use blocks and words, not plain text only.

pdfplumber as table/debug fallback. Use it when PyMuPDF block extraction is insufficient for tables.

OCRmyPDF/Tesseract as scan fallback. Trigger only when native text is absent or unusable.

PaddleOCR only for scanned table-heavy documents. Keep this optional because of dependency weight.

Docling/Marker/MinerU as research candidates. Useful for future RAG/Markdown/JSON workflows, but benchmark against your documents before integrating.

Cloud APIs only if local methods fail on enough real documents to justify cost/privacy trade-offs.

7.2 Internal data model



Use three layers internally:



1\. Preview text

2\. Structured page objects: blocks, words, tables, images, form fields

3\. Extracted fields with provenance and validation status



This lets the UI remain simple while the engine preserves enough information for robust extraction.



7.3 Do not overuse OCR



For digitally born PDFs, native parsing is more reliable than OCR. OCR is only the right answer when the document is image-only, has a bad OCR layer, or contains visual content that native extraction cannot read.



7.4 Add geometry-aware mapping methods over time



The current mapping methods are useful, but the next meaningful improvement would be adding:



Label Right;

Label Below;

Table Cell;

Page Region;

Regex Capture Group.



These would reduce the need for fragile line-number rules.



7.5 Export should be gated by required identity fields



For the CE workflow, Work Provider should be treated as a required export gate. If the provider is empty, the JSON export should be blocked for that document in both single and batch mode. This prevents image-only/unidentified documents from generating misleading exports.



8\. Evaluation framework



Build a gold test set containing:



clean digital instruction PDF;

table-heavy engineer report;

scanned PDF;

OCRed scan;

poor OCR scan;

multi-column report;

PDF with bad reading order;

PDF with hidden OCR layer;

form PDF;

image-only “document”;

batch import with one unidentified file;

engineer report overlay case.



Measure:



Metric	Purpose

Field exact match	Main business accuracy

Normalized field match	Dates, VRMs, mileage, postcode

False-positive export rate	Prevents bad JSON creation

Missing mandatory field rate	Identifies mapping/provider failures

Table cell accuracy	Table parser quality

OCR character error rate	Scan quality

Processing time	Desktop UX

Parser fallback rate	Pipeline health

Manual correction rate	Real-world usefulness



For your app, field-level accuracy is more important than whole-document text similarity. A perfect transcript that contaminates VRM with adjacent table columns is worse than a rough transcript that extracts all required fields correctly.



9\. Practical implementation hierarchy



The implementation priority should be:



Deterministic native extraction

PyMuPDF blocks/words.

Preserve page coordinates.

Avoid plain-text-only logic.

Field validation

Prevent bad exports.

Keep accepted states constrained.

Table-specific fallback

pdfplumber or PyMuPDF table finder.

Use only when needed.

OCR fallback

OCR image-only pages.

Avoid whole-document OCR for digital PDFs.

Advanced parser trial

Benchmark Docling, Marker, MinerU, PaddleOCR on a fixed CE gold set.

Cloud/VLM fallback

Use only if local deterministic extraction fails frequently enough to justify it.

10\. Key takeaways



The most important finding is that PDF parsing is not fundamentally a text problem; it is a visual-layout-to-structure problem. The PDF format itself does not reliably encode the semantics that business extraction needs. Native text extraction is still the first step, but production systems must preserve geometry, detect tables separately, apply OCR selectively, validate outputs, and keep provenance.



For CE Document Mapper, the practical answer is not to chase a single universal parser. The correct architecture is a controlled cascade: PyMuPDF geometry first, pdfplumber/table fallback, OCR fallback, optional advanced parsers, strict business validation, and export blocking for unidentified documents.

