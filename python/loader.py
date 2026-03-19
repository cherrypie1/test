import json
import time
import logging
import requests

from clickhouse_driver import Client

API_URL = "http://api.open-notify.org/astros.json"
MAX_RETRIES = 5

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_data():

    for attempt in range(1, MAX_RETRIES + 1):

        try:
            response = requests.get(API_URL, timeout=10)

            if response.status_code == 200:
                return response.json()

            if response.status_code == 429:
                wait = 2 ** attempt
                logger.warning(f"429 rate limit, retry in {wait}s")
                time.sleep(wait)
                continue

            raise Exception(f"Unexpected status {response.status_code}")

        except Exception as e:

            wait = 2 ** attempt
            logger.warning(f"Attempt {attempt} failed: {e}")
            time.sleep(wait)

    raise RuntimeError("Max retries exceeded")


def insert_data(client, data):

    payload = json.dumps(data)

    client.execute(
        "INSERT INTO raw_astros (raw_json) VALUES",
        [(payload,)]
    )

    logger.info("Inserted data into raw_astros")


def main():

    client = Client(
        host="localhost",
        port=9000,
        user="default",
        password="",
        database="default"
    )

    data = fetch_data()

    insert_data(client, data)


if __name__ == "__main__":
    main()