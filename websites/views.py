from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import WebsiteForm
import qrcode

from io import BytesIO

# Create your views here.

def home(request):
    image = None
    form = WebsiteForm()
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            qr = qrcode.make(data)
            buffer = BytesIO()
            qr.save(buffer, format = 'PNG')
            return HttpResponse(buffer.getvalue(), content_type='image/png')
    context = {'form': form}
    return render(request, 'websites/home.html', context)

    