import sqlite3
import json

from models import Location

def get_all_locations():
    """
    gets all locations from the database

    Returns:
        list: list of dicts of locations in database
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
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)

# Function with a single parameter
def get_single_location(id):
    """gets information for a single location

    Args:
        id (int): id of the location you want to get information about

    Returns:
        object: the location object
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
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    """adds new location object to the list

    Args:
        location (dict): location object to be added

    Returns:
        dict: the location object as added with the new id key
    """
    # # Get the id value of the last location in the list
    # max_id = ANIMALS[-1]["id"]

    # # Add 1 to whatever that number is
    # new_id = max_id + 1

    # # Add an `id` property to the location dictionary
    # location["id"] = new_id

    # # Add the location dictionary to the list
    # ANIMALS.append(location)

    # # Return the dictionary with `id` property added
    # return location

def delete_location(id):
    """removes location from the list

    Args:
        id (int): id of location to delete
    """
    # # Initial -1 value for location index, in case one isn't found
    # location_index = -1

    # # Iterate the ANIMALS list, but use enumerate() so that you
    # # can access the index value of each item
    # for index, location in enumerate(ANIMALS):
    #     if location["id"] == id:
    #         # Found the location. Store the current index.
    #         location_index = index

    # # If the location was found, use pop(int) to remove it from list
    # if location_index >= 0:
    #     ANIMALS.pop(location_index)

def update_location(id, new_location):
    """changes single location in the list

    Args:
        id (int): id of location to change
        new_location (dict): location object to be added
    """
    # # Iterate the ANIMALS list, but use enumerate() so that
    # # you can access the index value of each item.
    # for index, location in enumerate(ANIMALS):
    #     if location["id"] == id:
    #         # Found the location. Update the value.
    #         ANIMALS[index] = new_location
    #         break
