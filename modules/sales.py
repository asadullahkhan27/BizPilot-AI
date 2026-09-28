import pandas as pd

from database.database import get_connection
from database.models import add_lead


def get_leads():

    connection = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM leads
        ORDER BY id DESC
        """,
        connection
    )

    connection.close()

    return df


def get_sales_summary():

    df = get_leads()

    if df.empty:

        return {
            "count": 0,
            "pipeline": 0
        }

    return {
        "count": len(df),
        "pipeline": float(df["value"].sum())
    }


def add_sales_lead(
    customer,
    company,
    value,
    status,
    next_followup,
    notes
):

    add_lead(
        customer,
        company,
        value,
        status,
        next_followup,
        notes
    )
