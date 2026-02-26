from pydantic import BaseModel, Field, field_validator


class SalesOrder(BaseModel):
    order_id: int
    customer_name: str
    country: str
    product: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0.0)

    @field_validator("country")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Country cannot be empty")
        return v
