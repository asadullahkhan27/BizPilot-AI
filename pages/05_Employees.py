import streamlit as st

from modules.employees import (
    add_employee_record,
    get_employees,
    get_employee_summary
)


st.set_page_config(
    page_title="Employees",
    layout="wide"
)

st.title("Employee Management")


with st.form("employee_form"):

    name = st.text_input(
        "Employee Name"
    )

    department = st.text_input(
        "Department"
    )

    role = st.text_input(
        "Role"
    )

    salary = st.number_input(
        "Monthly Salary (PKR)",
        min_value=0.0,
        step=1000.0
    )

    status = st.selectbox(
        "Status",
        [
            "Active",
            "On Leave",
            "Inactive"
        ]
    )

    submit = st.form_submit_button(
        "Add Employee"
    )


if submit:

    if not name.strip():

        st.error(
            "Employee name is required."
        )

    else:

        add_employee_record(
            name,
            department,
            role,
            salary,
            status
        )

        st.success(
            "Employee added successfully."
        )

        st.rerun()


summary = get_employee_summary()


col1, col2 = st.columns(2)


col1.metric(
    "Employees",
    summary["count"]
)

col2.metric(
    "Monthly Payroll",
    f"Rs. {summary['payroll']:,.0f}"
)


st.dataframe(
    get_employees(),
    use_container_width=True,
    hide_index=True
)
