import requests


class UBeac:
    def __init__(self, url, uid):
        self._URL = url
        self._UID = uid

    def send_data(self, sensor_id: str, measurement):
        data = {
            "id": self._UID,
            "sensors": [{
                "id": sensor_id,
                "data": measurement
            }]
        }

        requests.post(self._URL, json=data)
