"""IngestorInterface ABC."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Base class for parsing files."""

    ext = None

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check the file."""
        ext = path.split('.')[-1].lower()
        return cls.ext == ext

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse files and return List[QuoteModel]."""
        pass
