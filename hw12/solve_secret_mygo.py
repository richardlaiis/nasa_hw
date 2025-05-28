from PIL import Image

image_file = "secret_mygo.png"
img = Image.open(image_file)
pixels = list(img.getdata())
flag = ""

for i in range(0, 100, 3):
    colors = list(pixels[i])+list(pixels[i+1])+list(pixels[i+2])
    tmp = ""
    for j in range(8):
        if colors[j] % 2 == 0:
            tmp = tmp + "0"
        else:
            tmp = tmp + "1"
    flag = flag+chr(int(tmp, 2))

print(flag)