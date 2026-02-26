import argparse
from datapipeline.services.ingestion_service import run_ingestion
from datapipeline.services.reporting_service import generate_report
from datapipeline.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="AI & Data Pipeline CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Ingest command
    ingest_parser = subparsers.add_parser("ingest")
    ingest_parser.add_argument("--file", required=True, help="Path to the Excel file")

    # Report command
    report_parser = subparsers.add_parser("report")
    report_parser.add_argument(
        "--type", required=True, help="Type of report (e.g., country)"
    )

    args = parser.parse_args()

    if args.command == "ingest":
        run_ingestion(args.file)
    elif args.command == "report":
        generate_report(args.type)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
