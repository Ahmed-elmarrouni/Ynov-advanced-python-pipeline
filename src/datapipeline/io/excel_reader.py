import pandas as pd
from typing import List, Dict, Any
from datapipeline.models import SalesOrder
import logging

logger = logging.getLogger(__name__)


def read_sales_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads Excel , validates columns
    """
    try:

        df = pd.read_excel(file_path)

        required_columns = [
            "order_id",
            "customer_name",
            "country",
            "product",
            "quantity",
            "price",
        ]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        valid_orders = []
        for _, row in df.iterrows():
            try:
                order = SalesOrder(**row.to_dict())
                valid_orders.append(order.model_dump())
            except Exception as e:
                logger.error(f"Validation failed for row: {row.get('order_id')} - {e}")

        logger.info(f"Successfully ingested {len(valid_orders)} rows from {file_path}")
        return valid_orders

    except Exception as e:
        logger.error(f"Failed to read Excel file: {e}")
        raise
