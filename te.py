from PIL import Image
import numpy as np
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


path= r"E:\360MoveData\Users\Administrator\Desktop\text.jpg"
im = Image.open(path)

data = np.array(im)
k = data.shape
txt = ""
for i in range(0,k[0],10):
    for j in range(0,k[1],10):
        txt += get_char(data[i][j][0],data[i][j][1],data[i][j][2])
    txt += '\n'

with open("test.txt","w") as f:
    f.write(txt)
f.close()

