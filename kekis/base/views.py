from django.shortcuts import render, redirect
from .models import Project, Image, Account, Buy
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
import string   
import random 


def home(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    context = {'account': account}
    return render(request, 'base/welcome.html', context)




def projects(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    p = True
    s = request.GET.get('s') if request.GET.get('s') != None else ''
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(Q(name__iregex=s) | Q(description__iregex=s))
    projects = projects.filter(Q(kvantum__icontains=q))
    context = {'projects': projects, 'account': account, 'home': p}
    return render(request, 'base/home.html', context)


def buy(request, pk):

    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        return redirect('/login/')    
    
    
    account = Account.objects.get(id=id_per)
    shop = Shop.objects.get(id=pk)
    if int(account.rank >= int(shop.price)):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        request.session['key'] = ran
        b = Buy(key=ran, name = str(account.name), size = str(account.size), type = str(shop.title))
        account.rank = int(account.rank) - int(shop.price)
        account.save(update_fields=["rank"])
        b.save()
    else:
        ran = "Вы бедны"
    account = Account.objects.get(id=id_per)
    shop = Shop.objects.get(id=pk)
    context = {'key': ran,
               'shop': shop,
               'account': account}
    return render(request, 'base/buy.html', context)


def project(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    project = Project.objects.get(id=pk)
    images = Image.objects.all()
    context = {'project': project,
               'images': images,
               'account': account}
    return render(request, 'base/project.html', context)



def account(request, pk):
    d = request.session.get('id')
    d = "/" + str(d) + "/"
    if d in str(request.path):
        account = Account.objects.get(id=pk)
        if account.isTeacher == False:
            account_ws = Account.objects.all()
            score = 0
            id_num = []
            rank_num = []
            for i in range(account_ws.count()):
                i += 1
                p = Account.objects.get(id=i)
                id_num.append(p.id)
                rank_num.append(p.rank)
            slovar_id_rank = dict(zip(id_num, rank_num))
            
            sorted_dict = {}
            sorted_keys = sorted(slovar_id_rank, key=slovar_id_rank.get, reverse=True)  # [1, 3, 2]
            for w in sorted_keys:
                    sorted_dict[w] = slovar_id_rank[w]
            a = 1
            for w in sorted_dict:
                bob = Account.objects.get(id=w)
                bob.score = a
                bob.save()
                a +=1


            context = {'account': account}
            return render(request, 'base/account.html', context)
        else:
            return redirect(f'/teacher/{pk}/')
    else:
        return redirect('/login/')
        
        
        

def login(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        accountf = Account.objects.get(id=id_per)
        if accountf.isTeacher == False:
            return redirect(f'/account/{id_per}/')
        else:
            return redirect(f'/teacher/{id_per}/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                usr_account = Account.objects.get(login=cd["login"])
            except Account.DoesNotExist:
                print("Error")
                return redirect('/login/')
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                response = redirect(f'/account/{id_usr}/')
                return response
            else:
                print("Error")

        else:
            print("Error")
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})
    



def rating(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        return redirect('/login/')
    account = Account.objects.get(id=id_per)
    rank  = Account.objects.all().order_by("-rank")
    context = {'person': rank, "account": account}
    return render(request, 'base/rating.html', context)

def shop(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    shop = Shop.objects.all().order_by("-price")
    context = {'account': account, "shop": shop}
    return render(request, 'base/shop.html', context)




def competitions(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    s = request.GET.get('s') if request.GET.get('s') != None else ''
    competitions = Competitions.objects.filter(Q(name__iregex=q) | Q(description__iregex=q) | Q(kvantum__icontains=q))
    competitions = competitions.filter(Q(name__iregex=s))
    account = Account.objects.get(id=id_per)
    print(request.path)
    p = True
    context = {'competitions': competitions, 'account': account, 'competition': p}
    return render(request, 'base/competitions.html', context)

def liked(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = Account.objects.get(id=id_per)
    else:
        account = Account.objects.get(id=2)
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.favorite.add(Competitions.objects.get(id=liked_id))
        account.save()
        return HttpResponse("<h1>Nice!</h1>")

def unliked(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = Account.objects.get(id=id_per)
    else:
        account = Account.objects.get(id=2)
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.favorite.remove(Competitions.objects.get(id=liked_id))
        account.save()
        return HttpResponse("<h1>Nice!</h1>")
    



def teacher(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])
        account = Account.objects.get(id=id_per)
        if account.isTeacher == True:
            context = {'account': account}
            return render(request, 'base/teacher.html', context)
        else:
            return redirect(f'/account/{id_per}')
    else:
        return redirect('/login')


def addproject(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        accountf = Account.objects.get(id=id_per)
        if accountf.isTeacher == False:
            return redirect('/')
    if request.method == 'POST':
        form = AddProject(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                form.save()
                return redirect('/projects/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error")
    else:
        form = AddProject()
    return render(request, 'base/newproject.html', {'form': form,'account': accountf})


def addaccount(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        accountf = Account.objects.get(id=id_per)
        if accountf.isTeacher == False:
            return redirect('/')
    if request.method == 'POST':
        form = AddAccount(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                form.save()
                return redirect(f'/teacher/{id_per}/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error")
    else:
        form = AddAccount()
    return render(request, 'base/newaccount.html', {'form': form,'account': account})

def points_change(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id', None)
        points = request.POST.get('points', None)
        account = Account.objects.get(id=student_id)
        account.rank = points
        account.save()
        return HttpResponse("<h1>Nice!</h1>")