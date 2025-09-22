import qrcode

# The website link you want to encode
url = "https://reeea-a-program-agenda.netlify.app/"

# Create and configure the QRCode object
qr = qrcode.QRCode(
    version=1,  # controls size (1 = 21x21 modules)
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,  # pixel size of each box
    border=4,     # thickness of border (boxes)
)
qr.add_data(url)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save as PNG
img.save("website_qr.png")