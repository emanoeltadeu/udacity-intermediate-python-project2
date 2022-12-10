"""To parse csv files."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Class to parse csv files."""

    ext = "csv"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file at and return List[QuoteModel]."""
        try:

            quotes_list = []
            df = pd.read_csv(path, header=0, sep=',')

            for indice, row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes_list.append(quote)

        except Exception as e:
            print(e)

        return quotes_list