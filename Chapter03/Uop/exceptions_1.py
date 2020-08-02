import logging#
import time

logger = logging.getLogger(__name__)

class Connector:

    def connect(self):
        return self

    @staticmethod
    def send(data):
        return data

class Event:
    def __init__(self, payload):
        self._payload = payload

    def decod(self):
        return f"decoded {self._payload}"

class DataTransport:

    retry_threshold: int = 5
    retry_n_times = 3

    def __init__(self, connector):
        self._connector = connector
        self._connection = None

    def deliver_event(self, event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        except ConnectionError as e:
            logger.info("connection error detected: %s", e)
            raise
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise

    def connect(self):
        for _ in range(self.retry_n_times):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(
                    "%S: attempting new connection in %is", e, self.retry_threshold
                )
            else:
                return self.connection

        raise ConnectionError(f"couldnt connect after {self.retry_n_times} times")

    def send(self, data):
        return self.connection.send(data)