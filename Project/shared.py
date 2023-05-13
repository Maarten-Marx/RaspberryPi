import json
import os

# Get the path to the file containing shared data
path = os.getenv("shared-path")


# Class for sharing data between multiple processes
# In this case, used for sharing data between the main application and the discord bot (trap state and close-count)
class Shared:
    # reading the file and returning an object
    @staticmethod
    def read_data():
        # Creating the file if it didn't exist yet
        if not os.path.isfile(path):
            with open(path, "w") as shared:
                shared.write("{}")

        with open(path, "r") as shared:
            return dict(json.loads(shared.read()))

    # Storing new data to the file
    @staticmethod
    def write_data(data: dict):
        with open(path, "w") as shared:
            shared.write(json.dumps(data))

    # Method to simplify reading data
    @staticmethod
    def get_property(name: str):
        data = Shared.read_data()
        return data.get(name)

    # Method to simplify writing data
    @staticmethod
    def set_property(name: str, val):
        data = Shared.read_data()
        data[name] = val

        Shared.write_data(data)
