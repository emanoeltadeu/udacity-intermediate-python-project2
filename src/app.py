"""This is the meme app by WEB.

Class modified by emanoeltadeu@gmail.com.
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine.MemeEngine  import MemeEngine
from QuoteEngine.Ingestor   import Ingestor 
from datetime import datetime

app = Flask(__name__)

meme = MemeEngine('./memes')


def setup():
    """Load all resources."""

    #all the quote files
    quote_path = "./_data/DogQuotes/"
    quote_files = []
    for root, dirs, files in os.walk(quote_path):
        quote_files = [os.path.join(root, name) for name in files]

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    img = requests.get(image_url)

    body = request.form['body']
    author = request.form['author']

    path = None

    try:

        img_file = f'meme_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}_url_web.jpeg'
        open(img_file, 'wb').write(img.content)
        path = meme.make_meme(img_file, body, author)
        os.remove(img_file)

    except Exception as e:
        print(f"Exception: {e}")

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()