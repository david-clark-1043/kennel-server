EMPLOYEES = [
        {
            "id": 1,
            "name": "David"
        },
        {
            "id": 2,
            "name": "Henry"
        }
]

def get_all_employees():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """gets information for a single employee

    Args:
        id (int): id of the employee you want to get information about

    Returns:
        object: the employee object
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
