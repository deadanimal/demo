import base64
import qrcode
import qrcode.image.svg
from qrcode.image.pure import PymagingImage

from io import BytesIO

def generate_image_qr_from_text(text):

    image_generated = qrcode.make(text, image_factory=PymagingImage)
    bytes_stream = BytesIO()
    image_generated.save(bytes_stream)
    image_string = "data:image/png;base64," + base64.b64encode(bytes_stream.getvalue()).decode()

    return image_string