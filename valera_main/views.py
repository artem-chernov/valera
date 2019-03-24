from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def delivery(request):
    return render(request, 'delivery.html')

def contacts(request):
    return render(request, 'contacts.html')

def lanny_mode(request):
        return render(request, 'lanny_mode.html')

def coeur_joie(request):
        return render(request, 'coeur_joie.html')
