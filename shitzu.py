from PIL import Image, ImageDrawimport os
 
def draw_happy_shih_tzu(output_path):# Create a 512x512 transparent canvassize = (512, 512)img = Image.new('RGBA', size, (255, 255, 255, 0))draw = ImageDraw.Draw(img)
 
if name == "main":output_file = "/home/wuying/accio/round-3/code/shih_tzu_draw.png"draw_happy_shih_tzu(output_file)