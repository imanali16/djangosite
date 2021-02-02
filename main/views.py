from django.shortcuts import render

def index(request):
    # data ={
    #     'title': 'Главная страница',
    #     'values' : ['Privet', 'kak dela'],
    #     'obj':{
    #         'car':'BMW',
    #         'bar':'NMW'
    #     }
    # }
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')