from PIL import Image

image = Image.open('PTU20_LIVE/ai_guy.webp')
new_size = (240, 240)
resized = image.resize(new_size)
resized.save('PTU20_live/Naujas_pic.jpg')