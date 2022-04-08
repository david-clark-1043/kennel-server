import sqlite3
import json

from models import Customer

def get_all_customers():
    """
    gets all customers from the database

    Returns:
        list: list of dicts of customers in database
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

# Function with a single parameter
def get_single_customer(id):
    """gets information for a single customer

    Args:
        id (int): id of the customer you want to get information about

    Returns:
        object: the customer object
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                        data['email'], data['password'])

        return json.dumps(customer.__dict__)

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def create_customer(customer):
    """adds new customer object to the list

    Args:
        customer (dict): customer object to be added

    Returns:
        dict: the customer object as added with the new id key
    """
    # # Get the id value of the last customer in the list
    # max_id = ANIMALS[-1]["id"]

    # # Add 1 to whatever that number is
    # new_id = max_id + 1

    # # Add an `id` property to the customer dictionary
    # customer["id"] = new_id

    # # Add the customer dictionary to the list
    # ANIMALS.append(customer)

    # # Return the dictionary with `id` property added
    # return customer

def delete_customer(id):
    """removes customer from the list

    Args:
        id (int): id of customer to delete
    """
    # # Initial -1 value for customer index, in case one isn't found
    # customer_index = -1

    # # Iterate the ANIMALS list, but use enumerate() so that you
    # # can access the index value of each item
    # for index, customer in enumerate(ANIMALS):
    #     if customer["id"] == id:
    #         # Found the customer. Store the current index.
    #         customer_index = index

    # # If the customer was found, use pop(int) to remove it from list
    # if customer_index >= 0:
    #     ANIMALS.pop(customer_index)

def update_customer(id, new_customer):
    """changes single customer in the list

    Args:
        id (int): id of customer to change
        new_customer (dict): customer object to be added
    """
    # # Iterate the ANIMALS list, but use enumerate() so that
    # # you can access the index value of each item.
    # for index, customer in enumerate(ANIMALS):
    #     if customer["id"] == id:
    #         # Found the customer. Update the value.
    #         ANIMALS[index] = new_customer
    #         break
