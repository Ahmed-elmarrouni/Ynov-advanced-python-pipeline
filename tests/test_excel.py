import pytest
import pandas as pd
from unittest.mock import patch
from datapipeline.io.excel_reader import read_sales_excel


def test_file_not_found():
    # I test that a missing file raises an error
    with pytest.raises(Exception):
        read_sales_excel("fake_file.xlsx")


@patch("datapipeline.io.excel_reader.pd.read_excel")
def test_missing_columns(mock_read):
    # I test that it catches missing columns (like 'country')
    mock_read.return_value = pd.DataFrame(
        {
            "order_id": [1],
            "customer_name": ["Alice"],
            "product": ["Laptop"],
            "quantity": [2],
            "price": [1200.0],
        }
    )

    with pytest.raises(ValueError, match="Missing required column: country"):
        read_sales_excel("dummy.xlsx")


@patch("datapipeline.io.excel_reader.pd.read_excel")
def test_successful_read(mock_read):
    # I test a successful data load
    mock_read.return_value = pd.DataFrame(
        {
            "order_id": [1],
            "customer_name": ["Alice"],
            "country": ["France"],
            "product": ["Laptop"],
            "quantity": [2],
            "price": [1200.0],
        }
    )

    result = read_sales_excel("dummy.xlsx")
    assert len(result) == 1
    assert result[0]["customer_name"] == "Alice"
