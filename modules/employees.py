import pandas as pd

from database.database import get_connection
from database.models import add_employee


def get_employees():

    connection = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM employees
        ORDER BY id DESC
        """,
        connection
    )

    connection.close()

    return df


def get_employee_summary():

    df = get_employees()

    if df.empty:

        return {
            "count": 0,
            "payroll": 0
        }

    return {
        "count": len(df),
        "payroll": float(df["salary"].sum())
    }


def add_employee_record(
    name,
    department,
    role,
    salary,
    status
):

    add_employee(
        name,
        department,
        role,
        salary,
        status
    )
