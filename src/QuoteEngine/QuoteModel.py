"""Class to encapsulate the body and author."""

class QuoteModel():
    """Create new quote model to encapsulate the body and author."""

    def __init__(self, body, author):
        """Initialize quote."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f"{self.body} - {self.author}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"QuoteModel(body={self.body!r}, name={self.author!r}")    