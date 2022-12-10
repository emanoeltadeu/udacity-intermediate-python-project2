"""To parse docx files."""

from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to parse docx files."""

    ext = "docx"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file at and return List[QuoteModel]."""
        try:

            docx_file = docx.Document(path)
            quotes_list = []
            
            for para in docx_file.paragraphs:
                if para.text != "":
                    parsed_text = para.text.split(' - ')
                    quote_model = QuoteModel(parsed_text[0], parsed_text[1])
                    quotes_list.append(quote_model)

        except Exception as e:
            print(e)

        return quotes_list