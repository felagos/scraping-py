import time
import threading
from typing import Dict
from urllib.parse import urlparse


class PolitenessPolicy:
    def __init__(self, delay_per_domain: float = 2.0):
        self.delay_per_domain = delay_per_domain
        self.last_request_time: Dict[str, float] = {}
        self.lock = threading.Lock()

    def wait_if_needed(self, url: str) -> None:
        domain = urlparse(url).netloc
        self.lock.acquire()

        try:
            current_time = time.time()
            last_time = self.last_request_time.get(domain, 0)

            time_since_last = current_time - last_time
            if time_since_last < self.delay_per_domain:
                sleep_time = self.delay_per_domain - time_since_last
                time.sleep(sleep_time)

            self.last_request_time[domain] = time.time()
        finally:
            self.lock.release()
