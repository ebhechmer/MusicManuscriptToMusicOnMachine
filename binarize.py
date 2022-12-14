from PIL import Image

def load_binarized_image(filename):
    with open(filename, "rb") as img_handle:
        img = Image.open(img_handle)
        img = img.convert('L')
        img = img.point( lambda p: 255 if p > 255//1.5 else 0 )
        #img = img.convert('1')
        img_data = img.getdata()
        if img.mode.startswith("RGB"):
            pixels = [
                round(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]) for p in img_data
            ]
        elif img.mode == "LA":
            pixels = [p[0] for p in img_data]
        elif img.mode == "L":
            pixels = list(img_data)
        else:
            raise ValueError("Unsupported image mode: %r" % img.mode)
        w, h = img.size
        return {"height": h, "width": w, "pixels": pixels}

def save_image(image, filename, mode="PNG"):
    out = Image.new(mode="L", size=(image["width"], image["height"]))
    out.putdata(image["pixels"])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()
def remove_staff(filename):
    with open(filename, "rb") as img_handle:
        img = Image.open(img_handle)
        img = img.convert('L')
        img_data = img.getdata()
        w, h = img.size
        pixels = list(img_data)
        stafflines = [0]*h
        for i in range(h):
            for j in range(w):
                stafflines[i] += pixels[w*i+j]
            if stafflines[i]<10*w:
                for j in range(w):
                    pixels[w*i+j]=255
        #print(stafflines)
        return {"height": h, "width": w, "pixels": pixels}
                
        

filename = '/Users/lawrenceliu/Downloads/IMG_0099.png'
pic = remove_staff(filename)
save_image(pic, '/Users/lawrenceliu/Downloads/IMG_0100.png')
