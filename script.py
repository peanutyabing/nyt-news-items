import argparse
import logging
from collections.abc import MutableMapping
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_ROOT = "https://api.nytimes.com/svc/search/v2/articlesearch."
API_KEY = os.environ.get("API_KEY")

"""
Skeleton for Squirro Delivery Hiring Coding Challenge
August 2021
"""


log = logging.getLogger(__name__)


class NYTimesSource(object):
    """
    A data loader plugin for the NY Times API.
    """

    def __init__(self):
        pass

    def connect(self, inc_column=None, max_inc_value=None):
        log.debug("Incremental Column: %r", inc_column)
        log.debug("Incremental Last Value: %r", max_inc_value)

    def disconnect(self):
        """Disconnect from the source."""
        # Nothing to do
        pass

    def getDataBatch(self, batch_size, config):
        """
        Generator - Get data from source on batches.

        :returns One list for each batch. Each of those is a list of
                 dictionaries with the defined rows.
        """
        # TODO: implement - this dummy implementation returns one batch of data
        all_articles = []
        batch = []
        page = 0

        while True:
            url = '%sjson?q=%s&page=%s&api-key=%s' % (
                API_ROOT, config["query"], page, config["api_key"])
            res = requests.get(url)

            if res.status_code == 200:
                pageResList = res.json()["response"]["docs"]

                for article in pageResList:
                    flattened_article = self.flatten_dict(article)
                    if len(batch) < batch_size:
                        batch.append(flattened_article)
                    else:
                        all_articles.append(batch)
                        batch = []
                page += 1

            else:
                break

        return all_articles

    def _flatten_dict_gen(self, d, parent_key, seperator):
        for key, val in d.items():
            new_key = parent_key + seperator + key if parent_key else key
            if isinstance(val, MutableMapping):
                yield from self.flatten_dict(val, new_key, seperator=seperator).items()
            else:
                yield new_key, val

    def flatten_dict(self, d: MutableMapping, parent_key: str = "", seperator: str = "."):
        return dict(self._flatten_dict_gen(d, parent_key, seperator))

    def getSchema(self):
        """
        Return the schema of the dataset
        :returns a List containing the names of the columns retrieved from the
        source
        """

        schema = [
            "title",
            "body",
            "created_at",
            "id",
            "summary",
            "abstract",
            "keywords",
        ]

        return schema


if __name__ == "__main__":
    config = {
        "api_key": API_KEY,
        "query": "Silicon Valley",
    }
    source = NYTimesSource()

    # This looks like an argparse dependency - but the Namespace class is just
    # a simple way to create an object holding attributes.
    # source.args = argparse.Namespace(**config)

    for idx, batch in enumerate(source.getDataBatch(10, config)):
        print(f"{idx} Batch of {len(batch)} items")
        for item in batch:
            print(f"  - {item['_id']} - {item['headline.main']}")
