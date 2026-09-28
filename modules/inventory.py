import pandas as pd

from database.database import get_connection
from database.models import add_inventory


def get_inventory():

    connection = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM inventory
        ORDER BY id DESC
        """,
        connection
    )

    connection.close()

    return df


def get_inventory_summary():

    df = get_inventory()

    if df.empty:

        return {
            "items": 0,
            "low_stock": 0,
            "stock_value": 0
        }

    low_stock = (
        df["quantity"] <= df["reorder_level"]
    ).sum()

    stock_value = (
        df["quantity"] * df["unit_price"]
    ).sum()

    return {
        "items": len(df),
        "low_stock": int(low_stock),
        "stock_value": float(stock_value)
    }


def add_inventory_item(
    product,
    sku,
    quantity,
    reorder_level,
    unit_price
):

    add_inventory(
        product,
        sku,
        quantity,
        reorder_level,
        unit_price
    )
