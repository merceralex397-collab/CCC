# AZT Paint Calculation — Method Reference

> **Source: AZT Automotive GmbH — Paint Calculation System Description (EN, 03 June 2020). Source PDF: `atzpaintcalculation.pdf` (this folder). Material costs are index-based (AZT Index 100) and country/currency/quarter adjusted.**

Distilled method + rules for computing collision-repair **paint time (hours)** and **paint material cost**. Consumed by `total-loss` and `repair-estimate`. This is a method reference, not the data tables — the per-part hour/material values live in AZT's type-specific tables and are continuously updated (they are deliberately omitted from the source description).

---

## Core philosophy

- **REFA time-study basis.** All working times are average values from time studies conducted per REFA methods and evaluated by repair stage. Material quantities come from repair studies, calculated per area for each case.
- **Paintable surface is the starting point.** Every time figure begins from the *paintable surface* — the condition in which the body worker hands the part to the painter (see Delivery condition).
- **Manufacturer- and vehicle-independent.** Values depend only on the vehicle surface (per dm²), the paint stage, the paint type, and the substrate — not on the vehicle or paint manufacturer. The same paint types, stages, and time/material specs apply unchanged to cars, off-road vehicles, vans, and transporters.
- **Index 100 material baseline.** AZT Index 100 = the material cost (in local currency, excl. VAT) for a paint job, being the average of country-specific workshop list prices across multiple paint/auxiliary-material manufacturers, before any discounts. Adjusted per country/currency and refreshed at least every 6 months. The user may apply an **individual index adjustment** to match their own conditions (see below). Material is **never** calculated as a percentage of the labour rate.

---

## Paint systems (paint types)

Times and materials are stated for two base groups; multi-coat builds reuse those values with multipliers.

| System | Build (up to top coat) |
|---|---|
| **1-coat solid / metallic** | single-coat 2C top coat |
| **2-coat solid / metallic / multi-effect** | base coat (solid, metallic, or multi-effect: mica/pearl/xirallic/etc.) + 2C clear coat, wet-in-wet |
| **3-coat** | adds either a **pre-painting** layer (uniform coverage, usually white) *or* a **coloured clear-coat** layer, before/with the standard 2-coat build |
| **4-coat** | combines **pre-painting + coloured clear coat** with the 2-coat build |

**Multi-coat calculation recipe** (build per part on top of the 2-coat, paint-stage I–IV base figure):

- **3-coat with pre-painting:** + pre-painting layer at **50%** of 1-coat surface paintwork (wet-in-wet) or **100%** (if pre-painting is dried & sanded).
- **3-coat, two clear coats:** + first (coloured) clear coat at **50%** (wet-in-wet) or **100%** (dried & sanded) of 1-coat surface paintwork.
- **4-coat:** pre-painting + first clear coat at **150%** of 1-coat surface paintwork; the 2-coat surface element at **150%**. Variants with dry-and-sand stages scale to **200%**.
- **No material surcharge** for multi-effect pigments — already included in the respective material figure. *(Exception: multi-effect pigment inclusion does NOT currently apply to these countries: AU, BA, CH, CZ, GB, GR, HR, HU, IE, IN, PL, RS, SK, SL, TR, ZA.)*

---

## Substrate paint stages

### Metal parts (stages I–IV) — VDA-uniform classification

| Stage | Meaning |
|---|---|
| **I** | New-part painting, complete application. Welding part (E, *Einschweißteil*) or installation part (M, *Montageteil*) — both rated stage I. |
| **II** | Surface painting (small surface damage, no filling, colour matching) **and** interior-part painting — identical time/material per dm², so one shared stage (II-a surface, II-b interior). |
| **III** | Repair painting with filler over **up to 50%** of the part surface. |
| **IV** | Repair painting with filler over **above 50%** of the part surface. |

Interior parts are defined as fixed composite components (e.g. engine compartment, wheel housing + longitudinal beam, rear panel, luggage-compartment floor) and must not be further sub-split by the user.

### Plastic parts (K-stages) — five stages, prefix "K"

| Stage | Meaning |
|---|---|
| **K1R** | New part **without** filler application |
| **K1N** | New part **with** filler application, **without** sanding |
| **K1G** | New part **with** filler, **with** sanding (PUR soft foam) |
| **K2** | Surface painting |
| **K3** | Repair paintwork |

K1R / K1N / K1G are the three new-part stages; K2 and K3 are the repair stages. The driver is the **delivery state + surface** of the part: unpainted/unfinished vs primed vs already painted, even vs structured, hard plastic vs PUR soft foam. Plastic is normally painted **dismounted**; plastic parts are **never** included in sectional-painting positions.

**Pre-painting grouping:** when painting *on the vehicle with pre-painting*, the applicable stages are metal **I** and plastic **K1R / K1N / K1G** (pre-painting of one or more parts dismounted / at the folds, and after adapting, mounting or welding).

---

## Delivery condition & preparation

**Delivery condition (paintable surface)** — the body worker hands over a defined surface:
1. Damaged areas flattened/welded to correct contour and edge, optionally with current body filler, finished with proper tools (no angle grinders) so the painter can start at random/orbital sanding (≈ P120 grain).
2. The painter then finishes in a **maximum of three filler stages** (e.g. polyester filler → fine filler → sanding filler, or polyester filler → polyester spray filler → sanding filler).

**Preparation for painting** — order-dependent (booked **once per order**, by painting process), covering: vehicle/part movement, tool & material prep/cleanup, colour sample & toning, surface check, booth setup/strip, PPE, evaporation, covering, and finishing (overspray/sanding-debris removal, masking-line cleanup, minor touch-ups by grind/polish on the freshly painted part). **Not included:** prep/polishing of adjacent surfaces, interior cleaning, vehicle wash.

**Masking (plastic):** plastic is usually painted dismounted, so masking is *not* in the base values. Add **0.2 h per part** for masking when a plastic part is mounted, only partially painted, has differently-coloured inlaid strips, or has built-in/mounted parts (e.g. mirrors).

---

## Calculation factors

A correct order-related figure requires settling each of these:

1. **Paintable surface** (per dm², from the type-specific table) — the size-independent driver of per-part time/material.
2. **Delivery condition** (paintable surface achieved; ≤3 filler stages).
3. **Paint type** — 1-coat / 2-coat / multi-layer (3- or 4-coat).
4. **Substrate & stage** — metal I/II/III/IV or plastic K1R/K1N/K1G/K2/K3.
5. **Painting process** — *on the vehicle without pre-painting* / *on the vehicle with pre-painting* / *only dismounted assembly parts*.
6. **Additional materials / preparation items** (each booked once per order where applicable):
   - **Mixing paint with mixing plant** (when ready-mix paint isn't used): ~0.2–0.3 h.
   - **Colour sample & final colour determination** (up to three sample sheets — light/medium/dark grey): ~0.2–0.3 h.
   - **2-colour paintwork** (see below).

**Principal vs Composite work** when both metal *and* plastic parts are painted in one order:
- **Rule 1:** the preparation that takes the most time is "Principal work"; the other material's prep is "Composite work" (a reduced figure).
- **Rule 2:** for *simultaneous* preparations, metal is always Principal work and plastic is always Composite work.

**Adding up:** all painting times and material costs are additive. Book "preparation for painting" once per order. Per-part surface time + material is booked per component.

---

## Surcharges & adjustments

- **Scratch-resistant clearcoat:** add **+0.3 h per horizontal component** (bonnet, roof, boot lid) and **+0.1 h per vertical component** (wing/mudguard, door) for extra sanding/polishing. No lump-sum charge. Significantly higher material in individual cases is handled via the material-index adjustment.
- **2-colour paintwork** (classic two-tone only — NOT design/strip/special painting). Contrasting **matt-black** areas on outer/inner body surfaces do **not** count as 2-colour work.
  - *Variation A:* complete part/section in stage & type of the first colour **+** the section surface in **stage II** in the second colour's paint type.
  - *Variation B:* first section in first colour's stage/type **+** second section in second colour's stage/type.
  - **+** preparation time/material for the stage & method, **plus** an additional **0.1 h** prep for the 2-colour work (and possibly extra mixing 0.2–0.3 h and colour-sample 0.2–0.3 h).
- **Individual index adjustment:** post-calculate ≥3 representative jobs at Index 100, compare to operation-specific actual material cost, and set `index = (cost at Index 100) / (operation-specific cost) × 100`. Re-check regularly. Loss/bulk/residual surcharges are already in AZT values — no adjustment needed for those.
- **Additional work** (separate time/material, not in base values): colour search on the vehicle, R&I of trim/assembly/body parts, exposing engine-compartment areas, removing wax/preservatives, underbody/sealing/cavity protection, interior-part painting, corrosion removal to reach a paintable surface, painting folds/inner surfaces in stage II/III repaints, painting offset-colour (matt-black) window frames/pillars, and removal/application of bonded trim or films.

---

## Multi-panel blending propagation (metallic / pearl / multi-effect)

The AZT method books, per part, *"+ possible blending of adjacent part"* and treats blending as the technique in which the new base/clear coat runs out **within** a component, with the old/new transition polished to align. The document does **not** enumerate specific panel-to-panel chains; the following are the standard practitioner conventions consistent with that rule and with how colour-match blending propagates on metallic/pearl finishes. **Apply judgment per damage, colour, and recipe — these are conventions, not verbatim AZT figures:**

- **Rear quarter (side panel rear)** → blend into the **rear door** and/or **C-pillar**; sometimes onto the **roof** where the quarter meets it.
- **Front wing** → blend into the **front door** and the **bonnet edge**.
- **Door** → blend into the **adjacent door** or the adjoining **quarter/wing**.
- **Bumper** → blend **across the face** of the bumper; rarely onto adjacent (body) panels.

Each blended adjacent panel is added as **2-coat surface paintwork** (the surface element of stage II), per the multi-coat recipe above. If two or more sections of a single part are painted, always charge the **whole part**.

---

## Spot / sectional painting

**Spot painting** (spot-repair / partial bumper-graze painting) — a blending method limited to the damage site; no full clear-coat over the part.
- **Useful for:** damage ≤3.5 cm (plus bumper side/corner sideswipes), max one damage point per part, **2-coat** paintwork, **on the vehicle only** (not dismounted parts), glossy finishes.
- **Not useful for:** 2-colour paintwork, powder-slurry 2-coat substrates.
- **Body-zone rule:** Zone A (horizontal: bonnet/upper shell/roof) — spot not useful; Zone B (vertical surfaces) — only useful near an edge with a suitable colour; Zone C (other exterior/interior/covered surfaces, bumpers) — useful without restriction.
- **Indicative values:** preparation for spot painting **0.5 h**; mixing **0.3 h**; colour sample **0.3 h**; **0.9 h per damaged area** (2 areas on one part = 1.8 h). The 0.5 h spot-prep is **dropped** as soon as any other paint job is applied on the vehicle (exception: a dismounted part painted separately keeps it). The per-component surface time + material is always charged.

**Sectional painting** — AZT defines fixed sectional positions per vehicle type that bundle all *serially painted metal parts* of a model in combination, preventing missing parts or double-counting. Use sectional items for larger repairs.

- **Cars / off-road:** *Front end* (all front panels + both front wings + front cover, ± cowl/ventilation/side parts) · *Car side* (front wing + front door + sill + rear side panel, ± rear door/wing) · *Rear end* (all rear panels + both rear side panels + rear cover/tailgate, ± cowl/rear wings) · *Complete without roof* (front + rear + all doors + both sills) · *Complete* (+ roof).
- **Vans / transporters:** *Front* (door-to-door incl. wing/corner, no front bumper) · *Side* (front to rear, no front/rear wings/corners, no tail lift) · *Rear* (side-to-side incl. rear corner, no rear bumper/tail lift). Sections combine; double-counting excluded. Also consider glazing, side door vs panel, one/two-piece tailgate, wheelbase, and roof height.
- **Plastic parts are never part of sectional positions** — cost them individually via the K-stage / special tables.

---

## How to use in an estimate (checklist)

1. **Identify panels** to be painted (body + attachments; metal vs plastic). For large jobs, prefer **sectional** items.
2. **Classify substrate & stage** per panel — metal I/II/III/IV (by filler %) or plastic K1R/K1N/K1G/K2/K3 (by delivery state/surface).
3. **Pick the paint system** — 1-coat / 2-coat / 3-coat / 4-coat; apply the multi-coat multipliers (50/100/150/200%).
4. **Set the process** per panel — on-vehicle without pre-painting / on-vehicle with pre-painting / dismounted.
5. **Add blend panels** for metallic/pearl/multi-effect — book adjacent panels as 2-coat surface paintwork (propagation conventions above).
6. **Apply surcharges & extras** — scratch-resistant clearcoat (+0.3 h horizontal / +0.1 h vertical), 2-colour (+0.1 h prep, excl. matt-black contrast), masking (+0.2 h/part on mounted plastic), and any "additional work."
7. **Book preparation once per order** (+ mixing 0.2–0.3 h and colour sample 0.2–0.3 h if used); resolve Principal vs Composite when mixing metal + plastic.
8. **Sum time + material.** Material = Index-100 figures × the (country/currency-adjusted, optionally operation-specific) material index; multiply painting hours by the labour rate. Material is never a % of labour.
