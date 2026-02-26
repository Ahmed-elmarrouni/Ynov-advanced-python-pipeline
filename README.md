# Ynov-advanced-python-pipeline

This is a professional Python data pipeline. It reads sales data from an Excel file, checks if the data is correct using Pydantic, and saves the clean data as a JSON file. It also connects to a PostgreSQL database to generate sales reports.

## Architecture

This project is built with a clean structure and has four main parts:

1. **Data Ingestion (`src/datapipeline/io`):** Reads the Excel file (`sales_data.xlsx`) using `pandas`.
2. **Data Validation (`src/datapipeline/models.py`):** Checks the rules and data types using `Pydantic`.
3. **Database (`src/datapipeline/database`):** Connects to a PostgreSQL database inside a Docker container using `psycopg2`.
4. **CLI (`src/datapipeline/cli.py`):** A Command Line Interface that lets you control the app easily from your terminal.

## Prerequisites

Before you start, make sure you have:

- Python 3.11 or higher
- Docker and Docker Compose
- Mac M1 (ARM64) or another compatible system

## Installation Steps

**1. Clone the project**

```bash
git clone [https://github.com/Ahmed-elmarrouni/Ynov-advanced-python-pipeline.git](https://github.com/Ahmed-elmarrouni/Ynov-advanced-python-pipeline.git)
cd Ynov-advanced-python-pipeline


```

2. Create a virtual environment and install libraries

```bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Start the database

```bash
docker compose up -d
```

4. Add the initial data to the database

```bash
docker exec -i data-pipeline-db-1 psql -U ahmed -d sales_db < postgres_seed.txt

```

## How to Use

First, tell your computer where to find the source code:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

```

**Command 1: Read and Clean the Data**
This command reads the Excel file, checks for errors, and saves a clean `validated_sales_data.json` file.

```bash
python -m datapipeline.cli ingest --file sales_data.xlsx

```

**Command 2: Generate a Report**
This command calculates the total revenue for each country from the database and prints a clean report.

```bash
python -m datapipeline.cli report --type country

```

## Testing

This project includes 10 automated tests using `pytest` to make sure everything works perfectly.

To run the tests:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest tests/

```
