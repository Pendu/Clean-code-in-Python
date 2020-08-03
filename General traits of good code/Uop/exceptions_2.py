import logging
import time

logger = logging.getLogger(__name__)

class Connector():

    def connect(self):
        return self

    @staticmethod
    def send(data):
        return data

class Event():
    def __init__(self,payload):
        self._payload = payload

    def decode(self):
        return f" decoded {self._payload}"

class connect_with_retry(Connector, retry_n_times, retry_threshold = 5):

    for _ in range(retry_n_times):
        try:
            return Connector.connect()
        except ConnectionError as e:
            logger.info(
                "%s: attempting new connection in %is" , e, retry_threshold
            )
            time.sleep(retry_threshold)
    exc = ConnectionError(f"Couldnt connect after {retry_n_times} times")
    logger.exception(exc)
    raise exc

class DataTransport:

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.conection = connection_with_retry(
            self._connector, self.retry_n_times, sefl.retry_threshold
        )
        self.send(event)
    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e )
            raise
