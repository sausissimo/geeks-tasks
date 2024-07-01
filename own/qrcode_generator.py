import qrcode
img = qrcode.make('')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode2.png")