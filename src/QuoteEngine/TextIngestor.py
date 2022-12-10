"""To parse txt files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse txt files."""

    ext = "txt"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the txt file at and return List[QuoteModel]."""
        try:

            file = open(path, "r")
            quotes_list = []

            for line in file.readlines():
                line = line.strip('\n\r').strip()
                line_length = len(line)

                if line_length > 0:
                    parsed_line = line.split(' - ')
                    quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                    quotes_list.append(quote_model)

        except Exception as e:
            print(f"Exception: {e}")

        return quotes_list
