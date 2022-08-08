
# modules
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Photo
import logging
from PIL import ImageFont, ImageDraw, Image
import config
from imgtoascii import image_to_ascii_art
# if u wanna use this create config file or variables with your api id and hash
app = Client("account" , api_id=config.api_id, api_hash=config.api_hash)
# enable logging
logging.basicConfig(level=logging.INFO)

# func for drawing

def asciiPhoto(text, imgw, imgh):
    image = Image.new("RGB", (imgw, imgh), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    txt = image_to_ascii_art('photomp.png')
    fontsize = 1  
    img_fraction = 45
    font = ImageFont.truetype("PTM75F.ttf", fontsize)
    # scaling font size
    while font.getsize(txt)[0] < img_fraction*image.size[0]:
        fontsize += 1
        font = ImageFont.truetype("PTM75F.ttf", fontsize)
    fontsize -= 1
    font = ImageFont.truetype("PTM75F.ttf", fontsize)
    draw.text((0, 0), txt, font=font, fill='black')
    image.save('done.png')

# handler for command !ascii
# use it with the photo!

@app.on_message(filters.me & filters.command(commands="ascii", prefixes="!"))
def ascii(client, message: Message):
    # yeah i am lazy so enter path to download yourself :)
    path = ?
    img = message.download(path, block=True)
    orig_width = message.photo.width
    orig_height = message.photo.height
    message.delete()
    asciiPhoto(image_to_ascii_art(img), orig_width, orig_height)
    message.reply_photo("done.png")

# app running(if ur dumb)
app.run()

