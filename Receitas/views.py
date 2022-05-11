from django.shortcuts import render


# Create your views here.
def home(Request):
    return render(Request, 'Receitas/pages/home.html')


def receitas(Request, id):
    return render(Request, 'Receitas/pages/receitas-views.html')
