from database.database import get_connection


def add_transaction(
    kind,
    category,
    amount,
    description,
    date
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO transactions
        (
            kind,
            category,
            amount,
            description,
            date
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            kind,
            category,
            amount,
            description,
            date
        )
    )

    connection.commit()
    connection.close()


def add_lead(
    customer,
    company,
    value,
    status,
    next_followup,
    notes
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO leads
        (
            customer,
            company,
            value,
            status,
            next_followup,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            customer,
            company,
            value,
            status,
            next_followup,
            notes
        )
    )

    connection.commit()
    connection.close()


def add_inventory(
    product,
    sku,
    quantity,
    reorder_level,
    unit_price
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO inventory
        (
            product,
            sku,
            quantity,
            reorder_level,
            unit_price
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            product,
            sku,
            quantity,
            reorder_level,
            unit_price
        )
    )

    connection.commit()
    connection.close()


def add_employee(
    name,
    department,
    role,
    salary,
    status
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO employees
        (
            name,
            department,
            role,
            salary,
            status
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            name,
            department,
            role,
            salary,
            status
        )
    )

    connection.commit()
    connection.close()
