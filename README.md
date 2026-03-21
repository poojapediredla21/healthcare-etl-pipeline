## About This Project
I built this project to simulate a real-world healthcare claims data pipeline based on my experience working with healthcare data, including claims, provider, and member datasets.

In many real-world scenarios, claims data is delivered as flat files and requires transformation into a structured format for reporting and analytics. In this project, I show how I design ETL pipelines to clean, model, and prepare claims data for downstream business use cases.

The goal of this project was to replicate how data engineering workflows operate in healthcare environments, including data standardization, dimensional modeling, and analytical querying.

# Healthcare Claims ETL Pipeline

An end-to-end ETL pipeline for simulated healthcare claims data using **Python**, **SQL**, and **SQLite** with **star schema modeling** for analytics.

## Overview
This project demonstrates how raw healthcare claims data can be ingested, cleaned, transformed, and loaded into dimensional and fact tables for downstream analytics and reporting.

The pipeline reads a raw claims dataset, standardizes and validates data fields, models the dataset into a warehouse-style schema, and loads the output into a SQLite database.

## Business Problem
Healthcare claims data is often delivered as flat files that are not analytics-ready. Reporting on claim performance, revenue, denials, and provider activity requires structured transformation and modeling.

This project simulates how a healthcare data engineering pipeline prepares claims data for business intelligence and analytical use cases.

## Tech Stack
- Python
- Pandas
- SQL
- SQLite
- GitHub

## Project Structure
```text
healthcare-etl-pipeline/
├── data/
│   ├── raw/
│   │   └── claim_data.csv
│   └── processed/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── model_data.py
│   ├── load.py
│   └── main.py
├── sql/
│   ├── create_tables.sql
│   └── analytics_queries.sql
├── docs/
├── requirements.txt
└── README.md
