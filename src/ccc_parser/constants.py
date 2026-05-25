from __future__ import annotations


FIELD_KEYS = [
    "work_provider",
    "vrm",
    "vehicle_model",
    "claimant_name",
    "reference",
    "incident_date",
    "instruction_date",
    "inspection_date",
    "inspection_address",
    "accident_circumstances",
    "vat_status",
    "mileage",
    "mileage_unit",
]

FIELD_LABELS = {
    "work_provider": "Work Provider",
    "vrm": "VRM",
    "vehicle_model": "Vehicle Model",
    "claimant_name": "Claimant Name",
    "reference": "Reference",
    "incident_date": "Incident Date",
    "instruction_date": "Instruction Date",
    "inspection_date": "Inspection Date",
    "inspection_address": "Inspection Address",
    "accident_circumstances": "Accident Circumstances",
    "vat_status": "VAT Status",
    "mileage": "Mileage",
    "mileage_unit": "Mileage Unit",
}

EVA_FIELD_ORDER = FIELD_KEYS[:]
EVA_LABEL_ORDER = [FIELD_LABELS[key] for key in FIELD_KEYS]

DATE_FIELDS = {"incident_date", "instruction_date", "inspection_date"}
REQUIRED_EXPORT_FIELDS = {"work_provider", "vrm", "inspection_address"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".tiff", ".webp", ".heic"}
DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".doc", ".msg", ".eml", ".txt", ".md", ".json"}
