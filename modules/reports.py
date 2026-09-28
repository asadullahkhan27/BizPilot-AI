from modules.finance import get_financial_summary
from modules.sales import get_sales_summary
from modules.inventory import get_inventory_summary
from modules.employees import get_employee_summary


def build_business_report():

    finance = get_financial_summary()
    sales = get_sales_summary()
    inventory = get_inventory_summary()
    employees = get_employee_summary()

    report = f"""
BIZPILOT AI
BUSINESS REPORT

========================

FINANCE

Revenue:
Rs. {finance['revenue']:,.2f}

Expenses:
Rs. {finance['expenses']:,.2f}

Profit:
Rs. {finance['profit']:,.2f}


========================

SALES

Leads:
{sales['count']}

Pipeline:
Rs. {sales['pipeline']:,.2f}


========================

INVENTORY

Items:
{inventory['items']}

Low Stock:
{inventory['low_stock']}

Stock Value:
Rs. {inventory['stock_value']:,.2f}


========================

EMPLOYEES

Employees:
{employees['count']}

Monthly Payroll:
Rs. {employees['payroll']:,.2f}

========================
"""

    return report
