def calculate_profit(
    revenue,
    expenses
):

    return revenue - expenses


def calculate_profit_margin(
    revenue,
    expenses
):

    if revenue == 0:

        return 0

    profit = revenue - expenses

    return (
        profit / revenue
    ) * 100
