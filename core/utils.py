import qrcode
import os
from django.conf import settings

def generate_qr_code(data, filename):
    img = qrcode.make(data)
    qr_path = os.path.join('qr_codes', filename)  # Save inside media/qr_codes/
    full_path = os.path.join(settings.MEDIA_ROOT, qr_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    img.save(full_path)

    return qr_path  # return relative path for saving in model
