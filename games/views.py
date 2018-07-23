from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'templates/home.html', context)
