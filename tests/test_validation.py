import pytest
from pydantic import ValidationError
from datapipeline.models import SalesOrder


def test_valid_sales_order():
    # I test that a normal order works perfectly
    order = SalesOrder(
        order_id=1,
        customer_name="Alice",
        country="France",
        product="Laptop",
        quantity=2,
        price=1200.0,
    )
    assert order.order_id == 1
    assert order.country == "France"


@pytest.mark.parametrize("invalid_qty", [0, -5])
def test_invalid_quantity(invalid_qty):
    # I test that quantity cannot be 0 or negative
    with pytest.raises(ValidationError):
        SalesOrder(
            order_id=2,
            customer_name="Bob",
            country="Morocco",
            product="Mouse",
            quantity=invalid_qty,
            price=25.0,
        )


@pytest.mark.parametrize("invalid_price", [0.0, -10.5])
def test_invalid_price(invalid_price):
    # I test that price cannot be 0 or negative
    with pytest.raises(ValidationError):
        SalesOrder(
            order_id=3,
            customer_name="Charlie",
            country="USA",
            product="Keyboard",
            quantity=1,
            price=invalid_price,
        )


def test_empty_country():
    # I test that the country cannot be an empty string
    with pytest.raises(ValidationError):
        SalesOrder(
            order_id=4,
            customer_name="David",
            country="   ",
            product="Monitor",
            quantity=1,
            price=300.0,
        )


def test_missing_fields():
    # I test that missing mandatory fields raises an error
    with pytest.raises(ValidationError):
        SalesOrder(order_id=5)
