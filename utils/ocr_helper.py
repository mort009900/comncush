from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_path):
    font = ImageFont.load_default()
    lines = text.split("\n")
    width = max(font.getsize(line)[0] for line in lines) + 20
    height = len(lines) * (font.getsize(lines[0])[1] + 5) + 20

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    y = 10
    for line in lines:
        draw.text((10, y), line, fill="black", font=font)
        y += font.getsize(line)[1] + 5

    image.save(output_path)
