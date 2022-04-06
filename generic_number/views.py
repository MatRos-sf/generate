from django.shortcuts import render
from .forms import RangeForms, ListForms, RandomPassword
from random import randint
from .random_tools import tools

def home_page(request):
    return render(request, "generic_number/home.html")


def random_number(request):
    drew = []
    if request.method == "POST":
        form = RangeForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a = cd['a']
            b = cd['b']
            amount = cd['amount']
            drew = tools.random_number(a,b,amount)

    else:
        form = RangeForms()
    return render(request, "generic_number/generic.html", {"form": form,
                                                           "drew": drew})





def random_list(request):
    drew = []
    if request.method == 'POST':
        form = ListForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            amount = cd['amount']
            arr = cd['list_random'].splitlines()
            arr = [i for i in arr if i]
            repeat = cd['repeat']
            print(repeat)

            drew = tools.draw_list(arr, amount, repeat)
            print(drew)
    else:
        form = ListForms()

    return render(request,"generic_number/generic_list.html",{"form": form,
                                                              "drew": drew})





def dice(request):
    throw = ''
    print(request.GET)
    if request.GET.get('Click'):
        throw = tools.throw_a_dice()
        print(throw)
    return render(request, "generic_number/generic_dice.html",{"throw": throw})



def toss_a_coin(request):
    choiced = False
    if request.GET.get("Click"):
        choiced = tools.heads_or_tails()

    return render(request,'generic_number/toss_a_coin.html', {'choiced': choiced})

def generic_password(request):

    new_password = ''
    if request.method == 'POST':
        form = RandomPassword(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            year = cd['year_birthday']
            prefix = cd['add_prefix']
            new_password = tools.generic_password(name,year,prefix)
    else:
        form = RandomPassword()
    return render(request,'generic_number/generic_password.html', {'form':form,
                                                                   'password': new_password})