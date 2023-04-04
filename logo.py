from PIL import Image, ImageDraw

h, w = 200, 400

image = Image.new("RGB", (w, h), "black")
draw = ImageDraw.Draw(image)

draw.ellipse([65, 55, 155, 145], outline="white", width=5)
draw.ellipse([125, 55, 215, 145], outline="white", width=5)
draw.ellipse([185, 55, 275, 145], outline="white", width=5)
draw.ellipse([245, 55, 335, 145], outline="white", width=5)

image.save("logo.png")


