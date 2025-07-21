from django.db import models
import qrcode
from PIL import Image
from django.core.files import File
from io import BytesIO
# Create your models here.


class Website(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        # Create a QR code from the website name and convert it to RGB
        qrcode_img = qrcode.make(self.name).convert('RGB')

        # Create a white 300x300 canvas
        canvas = Image.new('RGB', (300, 300), 'white')
        canvas.paste(qrcode_img)

        # Define filename for the QR code image
        fname = f'qrcode-{self.name}.png'

        # Create an in-memory buffer to save the image
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')

        # Save the image to the model's ImageField (qr_code)
        self.qr_code.save(fname, File(buffer), save=False)

        # Close the canvas to release resources
        canvas.close()

        # Save the model instance to the database
        super().save(*args, **kwargs)
