import requests


# Simple class for sending requests to uBeac
class UBeac:
    def __init__(self, url, uid):
        # Storing the provided info
        self._URL = url
        self._UID = uid

    def send_data(self, sensor_id: str, measurement):
        # Format the data correctly
        data = {
            "id": self._UID,
            "sensors": [{
                "id": sensor_id,
                "data": measurement
            }]
        }

        # Send the data to uBeac
        requests.post(self._URL, json=data)
