from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')
def gallery(request):
    return render(request, 'gallery.html')