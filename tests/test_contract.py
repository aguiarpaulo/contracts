import pytest
from datetime import datetime
from src.contract import Sales
from pydantic import ValidationError

def test_sales_data_check():
    """
    This test verifies that the Sales class correctly accepts and stores the valid data provided.
    Valid data includes a correct email, current date, positive value, product name, positive quantity
    and an existing category. The test confirms that the values stored in the instance match the data provided.
    """
    data_check = {
                "email": "comprador@example.com",
                "date": datetime.now(),
                "value": 100.50,
                "product": "Product X",
                "quantity": 3,
                "category": "category 3",
            }

    sales = Sales(**data_check)

    assert sales.email == data_check["email"]
    assert sales.date == data_check["date"]
    assert sales.value == data_check["value"]
    assert sales.product == data_check["product"]
    assert sales.quantity == data_check["quantity"]
    assert sales.category == data_check["category"]

def test_sales_invalid_data_check():
    invalid_data_check = {
            "email": "comprador",
            "date": "it is not date",
            "value": -100,
            "product": "",
            "quantity": -1,
            "category": "category 3",
        }
    
    with pytest.raises(ValidationError):
        Sales(**invalid_data_check)

def test_category_invalid_data_check():
    category_invalid_data_check = {
            "email": "comprador@example.com",
            "date": datetime.now(),
            "value": 100.50,
            "product": "Product X",
            "quantity": 3,
            "category": "Not Valid",
        }
    
    with pytest.raises(ValidationError):
        Sales(**category_invalid_data_check)