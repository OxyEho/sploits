from PIL import Image


img = Image.open("res.png")
res = []
for i in range(img.size[1]):
    for j in range(img.size[0]):
        pixel = img.getpixel((j,i))
        res.append(str(pixel[3] % 2))
res = "".join(res)
with open("flagg.bmp", "wb") as f:
    for i in range(0, len(res), 8):
        f.write(int(res[i:i+8], 2).to_bytes(1, "big"))
