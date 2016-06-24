from django.shortcuts import render

# Create your views here.
def angkasa_view(request):
    return render(request, 'angkasa/deep-minified.html', {})

def angkasasatu_view(request):
    return render(request, 'angkasa/no-jquery.html', {})

def angkasadua_view(request):
    return render(request, 'angkasa/with-jquery.html', {})
