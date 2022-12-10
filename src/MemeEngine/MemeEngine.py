"""The Meme Engine Module is responsible for manipulating and drawing text onto images."""

from datetime import datetime
import os
from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine:
    """Responsible for manipulating and drawing text onto images."""

    def __init__(self, output_path):
        """Create an instance of class."""
        self.output_path = output_path

    def make_meme(self, path, text, author, width=500) -> str:
        """Create the beautiful meme, finally."""
        try:
            img = Image.open(path)
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

            #choosing a random font
            fontes = "./_data/fontes/"
            fontes_files = []
            for root, dirs, files in os.walk(fontes):
                fontes_files = [os.path.join(root, name) for name in files]
    
            fonte_path = random.choice(fontes_files)              

            draw = ImageDraw.Draw(img)
            draw.text((10, img.size[1]-150), 
                f'{text}\n- {author}', 
                font=ImageFont.truetype(fonte_path, int(height/22)), 
                fill='black'
            )
            
            out_path = f'{self.output_path}/meme_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}.jpeg'
            
            img.save(out_path)
            print(f"Finally! Path to see the meme:")
            return out_path

        except Exception as e:
            print(f'Exception: {e}')