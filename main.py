from PIL import Image
from page import Paper


last_character_position = (0, 0) # line number and pixels from margin
sheet = Paper()
# Image.open(r"./b.png") = Image.open(r"./b.png")
sheet.draw_page_PIL(sheet, False)
# Image.open(r"./b.png") = Image.open(r"./b.png").resize((10, 10))
b = Image.open(r"./b.png")
b = b.resize((int(b.height * (sheet.line_height/b.height)), sheet.line_height))
bm = b.split()[3]

Image.Image.paste(sheet.img, b, (sheet.margin_top + (last_character_position[0] * sheet.line_height), sheet.margin_left + last_character_position[1]), bm)
sheet.img.save("OnResizeOutput.png")