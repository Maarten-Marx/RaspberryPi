import json
import os

path = os.getenv("shared-path")


class Shared:
    @staticmethod
    def read_data():
        if not os.path.isfile(path):
            with open(path, "w") as shared:
                shared.write("{}")

        with open(path, "r") as shared:
            return dict(json.loads(shared.read()))

    @staticmethod
    def write_data(data: dict):
        with open(path, "w") as shared:
            shared.write(json.dumps(data))

    @staticmethod
    def get_property(name: str):
        data = Shared.read_data()
        return data.get(name)

    @staticmethod
    def set_property(name: str, val):
        data = Shared.read_data()
        data[name] = val

        Shared.write_data(data)
