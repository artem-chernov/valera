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

def anna_jolly(request):
        return render(request, 'anna_jolly.html')

def diorella(request):
        return render(request, 'diorella.html')

def donafen(request):
        return render(request, 'donafen.html')

def weicy(request):
        return render(request, 'weicy.html')

def kaminnya(request):
        return render(request, 'kaminnya.html')