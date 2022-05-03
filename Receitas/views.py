from django.shortcuts import render


# Create your views here.
def home(Request):
    return render(Request, 'Receitas/home.html')
