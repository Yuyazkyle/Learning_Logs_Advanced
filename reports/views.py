from django.shortcuts import render
from .die_visual import plot
def index(request):
    return render(request, 'reports/index.html')

def dice_roll_result(request):
    '''Lets try import the die visual here'''
    #bar = plot()
    return render(request, 'reports/one_die.html')

def dice_roll(request):
    '''refreshes the plot and generates a new one'''
    bar = plot()