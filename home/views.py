from django.shortcuts import render


def home(request):
    '''
    Render Homepage
    '''
    return render(request, 'home/index.html')

def women_tech(request):
    '''
    Render women in tech page
    '''
    return render(request, 'home/women_in_tech.html') 

