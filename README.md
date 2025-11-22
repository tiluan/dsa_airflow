# Airflow Data Science Academy (DSA) Projects

This repository contains Apache Airflow projects developed as part of the Data Science Academy (DSA) course. It demonstrates various ETL pipelines and Airflow concepts.

## Prerequisites

- Docker
- Docker Compose

## Projects

### Project 1: Introduction to Airflow

Basic DAG examples to understand Airflow concepts like DAG definition, operators, and scheduling.

- **Location**: `dags/proj01/`
- **Key Files**: `DAG_01.py` (Hello World), `DAG_02.py`, etc.

### Project 2: ETL with BashOperator

An ETL pipeline that extracts data using shell scripts, transforms it, and loads it into a SQLite database.

- **Location**: `dags/proj02/`
- **Key Files**: `p2-etl.py`, `p2-etl.sh`, `p2-insert-sqlite.sh`

### Project 3: API Data Extraction

A Python-based ETL pipeline that extracts weather data from an API, transforms it using Pandas, and saves it to both CSV and SQLite.

- **Location**: `dags/proj03/`
- **Key Files**: `p3_dag.py`, `p3_etl.py`

## How to Run

1. **Download**: Clone or download this repository.
2. **Setup**: Navigate to the project directory.
3. **Initialize**: Run the following command to initialize Airflow and its database:

   ```bash
   docker compose up airflow-init
   ```

4. **Start**: Start the Airflow services:

   ```bash
   docker compose up
   ```

5. **Access**: Open your browser and go to [http://localhost:8080/login](http://localhost:8080/login).
   - **User**: `airflow`
   - **Password**: `airflow`

> **Note**: If you have a local PostgreSQL instance running on port 5432, stop it to avoid port conflicts.
