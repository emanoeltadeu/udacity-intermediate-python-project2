"""To parse pdf files."""

import subprocess
import random
import os
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse pdf files."""

    ext = "pdf"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the PDF file at and return List[QuoteModel]."""
        quotes_list = []

        try:

            tmp = f'./memes/{random.randint(0, 1000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])

            with open(tmp, 'r') as file:
                file_lines_content = file.readlines()

                for line in file_lines_content:
                    line = line.strip('\n\r').strip()
                    line_length = len(line)

                    if line_length > 0:
                        parsed_line = line.split(' - ')
                        quote_model = QuoteModel(parsed_line[0],
                                                 parsed_line[1])
                        quotes_list.append(quote_model)

            os.remove(tmp)
            return quotes_list

        except Exception as e:
            print(f'Exception: {e}')
