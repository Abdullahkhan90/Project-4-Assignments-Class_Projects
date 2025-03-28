## Created QR Code Project By Abdullah:

import qrcode

data = 'QR code using make() function'
img = qrcode.make(data)
img.save('my qr code project.png')