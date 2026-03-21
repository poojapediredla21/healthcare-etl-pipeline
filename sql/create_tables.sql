-- Dimension Tables

CREATE TABLE dim_patient (
    patient_id TEXT PRIMARY KEY
);

CREATE TABLE dim_provider (
    provider_id TEXT PRIMARY KEY
);

CREATE TABLE dim_procedure (
    procedure_code TEXT PRIMARY KEY
);

CREATE TABLE dim_diagnosis (
    diagnosis_code TEXT PRIMARY KEY
);

CREATE TABLE dim_insurance (
    insurance_type TEXT PRIMARY KEY
);

CREATE TABLE dim_date (
    date_of_service DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- Fact Table

CREATE TABLE fact_claims (
    claim_id TEXT PRIMARY KEY,
    provider_id TEXT,
    patient_id TEXT,
    procedure_code TEXT,
    diagnosis_code TEXT,
    insurance_type TEXT,
    date_of_service DATE,
    billed_amount REAL,
    allowed_amount REAL,
    paid_amount REAL,
    claim_status TEXT,
    reason_code TEXT,
    follow_up_required TEXT,
    ar_status TEXT,
    outcome TEXT
);
