from django.shortcuts import redirect

def index(request):
    return redirect('/ordering')

def dashboard(request):
    return redirect('/ordering/dashboard')