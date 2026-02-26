import logging
from datapipeline.database.queries import get_revenue_by_country

logger = logging.getLogger(__name__)


def generate_report(report_type: str):
    logger.info(f"Generating report for: {report_type}")

    if report_type == "country":
        results = get_revenue_by_country()
        print("\n--- Revenue by Country ---")
        for row in results:
            # We handle both tuple and dict cursor returns safely
            country = row["country"] if isinstance(row, dict) else row[0]
            revenue = row["total_revenue"] if isinstance(row, dict) else row[1]
            print(f"{country}: ${revenue:,.2f}")
        print("--------------------------\n")
        logger.info("Report generated successfully.")
    else:
        logger.error(f"Unknown report type: {report_type}")
