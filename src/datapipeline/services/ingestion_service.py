from datapipeline.io.excel_reader import read_sales_excel
from datapipeline.database.connection import get_db_connection
import logging
import json

logger = logging.getLogger(__name__)


def run_ingestion(file_path: str):
    logger.info(f"Starting to process the file: {file_path}")

    # 1. Read and Validate the Excel data
    data = read_sales_excel(file_path)

    # 2. Save transformed output as JSON
    output_path = "validated_sales_data.json"
    with open(output_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Successfully saved validated data to {output_path}")

    # 3. Test the DB connection to be safe
    conn = get_db_connection()
    cur = conn.cursor()
    logger.info("Database connection is working perfectly.")

    cur.close()
    conn.close()
    logger.info("Ingestion process completed successfully.")
