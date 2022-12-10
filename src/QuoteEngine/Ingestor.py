"""Implementation subclass of IngestorInterface."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Subclasse de IngestorInterface(ABC)."""

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse file."""
        try:

            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)

            raise Exception("Invalid File Format")

        except Exception as e:
            print(e)
