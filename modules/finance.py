import pandas as pd

from database.database import get_connection
from database.models import add_transaction


def get_transactions():

    connection = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM transactions
        ORDER BY date DESC, id DESC
        """,
        connection
    )

    connection.close()

    return df


def get_financial_summary():

    df = get_transactions()

    if df.empty:

        return {
            "revenue": 0,
            "expenses": 0,
            "profit": 0
        }

    revenue = df.loc[
        df["kind"] == "Revenue",
        "amount"
    ].sum()

    expenses = df.loc[
        df["kind"] == "Expense",
        "amount"
    ].sum()

    return {
        "revenue": float(revenue),
        "expenses": float(expenses),
        "profit": float(revenue - expenses)
    }


def add_finance_record(
    kind,
    category,
    amount,
    description,
    date
):

    add_transaction(
        kind,
        category,
        amount,
        description,
        date
    )
