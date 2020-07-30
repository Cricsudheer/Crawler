from django.shortcuts import render , redirect, HttpResponse
from . import forms
from crawler.forms import UserProfileInfoForm,UserForm
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'crawler/index.html')

@login_required
def special(request):
    return  HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('crawler:index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('crawler:index'))

            else:
                return HttpResponse("inactive")
        else:
            return HttpResponse("Someone tried to login and failed")
    else:

        return render(request, 'crawler/login.html', {})   


def search_form_view(request):
    if request.method == 'POST':
        form = forms.searchform(request.POST)
        if form.is_valid():
            handle = form.cleaned_data.get('name')
            return redirect('/formpage/' + handle)
    else:
        form = forms.searchform()

    return render(request, 'crawler/searchpage.html', {'form': form})


import requests
from bs4 import BeautifulSoup


def contest_extr(r_ex,username):
    arr = [username]
    contest_no = r_ex[0].text.strip()
    arr.append(contest_no)
    contest_name = r_ex[1].find('a')['title'].strip()
    arr.append(contest_name)
    rank = r_ex[2].find('a').text.strip()
    arr.append(rank)
    solved = r_ex[3].find('a').text.strip()
    arr.append(solved)
    ratinf_change = r_ex[4].find('span').text.strip()
    arr.append(ratinf_change)
    new_rating = r_ex[5].text.strip()
    arr.append(new_rating)
    return arr




def person(request, handle):
    username = handle
    contest_url = 'https://codeforces.com/contests/with/' + username
    page = requests.get(contest_url, verify=True)
    if page.status_code != 200:
        return HttpResponse("UsernotFound")
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    contests = soup.find('div', attrs={"class": "datatable"})
    ctable = contests.find('tbody')
    list1 = contests.find_all('tr')
    totalcontest = len(list1) - 1
    print(f"{username} has participated in {totalcontest} contest ")
    conno = []
    connane = []
    rank = []
    solved = []
    rating_ch = []
    new_rati = []
    for i in range(totalcontest + 1):
        if i == 0: continue
        row = list1[i]
        r_ex = row.find_all('td')
        info = contest_extr(r_ex,username)
        conno.append(info[1])
        connane.append(info[2])
        rank.append(info[3])
        solved.append(info[4])
        rating_ch.append(info[5])
        new_rati.append(info[6])
    rating_stuff = {
        'conno': conno,
        'connane': connane,
        'rank': rank,
        'solved': solved,
        'rating_ch': rating_ch,
        'new_rati': new_rati,
    }
    return render(request,'crawler/demo.html',rating_stuff)


def register(request):

    registered =  False
    if request.method=="POST":
        user_form = UserForm(data = request)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and  profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit= False)
            profile.user= user

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.erros)
    else:
        user_form = UserForm()
        profile_form= UserProfileInfoForm()

    return render(request,'crawler/registration.html',
                  {'user_form':user_form},
                  {'profile_form': profile_form},
                  {'registered':registered})


