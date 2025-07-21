from django.shortcuts import render,redirect
from .forms import WebsiteForm
from .models import Website

# Create your views here.

def home(request):
    websites = Website.objects.all()
    form = WebsiteForm()
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'websites': websites}
    return render(request, 'websites/home.html', context)

def qrcode(request,pk):
    website = Website.objects.get(id=pk)
    context = {'website': website}
    return render(request, 'websites/qrcode.html', context)
    