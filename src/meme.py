"""This is the meme app by CLI.

Class modified by emanoeltadeu@gmail.com.
"""

import os
import random
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.Ingestor import Ingestor
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path, a body and author quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img_path = random.choice(imgs)
    else:
        img_path = path

    if body is None:

        # all the quote files
        quote_path = "./_data/DogQuotes/"
        quote_files = []
        for root, dirs, files in os.walk(quote_path):
            quote_files = [os.path.join(root, name) for name in files]

        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)

    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./memes')
    print("Making a meme for you...")
    path = meme.make_meme(img_path, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Welcome to Meme Generator Application!")

    parser.add_argument('--path', type=str,
                        default=None, help="image file path")

    parser.add_argument('--body', type=str,
                        default=None, help="body to add to the image")

    parser.add_argument('--author', type=str,
                        default=None, help="author to add to the image")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
