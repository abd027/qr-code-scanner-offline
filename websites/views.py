from django.shortcuts import render
from django.http import HttpResponse
from .forms import WebsiteForm
import qrcode
import base64
from io import BytesIO

def home(request):
    qr_image_base64 = None
    form = WebsiteForm()
    
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            qr = qrcode.make(data)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')

            # Rewind the buffer before reading
            buffer.seek(0)

            # Encode to base64
            img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            qr_image_base64 = f'data:image/png;base64,{img_base64}'

    context = {'form': form, 'qr_image': qr_image_base64}
    return render(request, 'websites/home.html', context)
