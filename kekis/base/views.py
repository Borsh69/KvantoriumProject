from django.shortcuts import render, redirect
from .models import Project, Image, Account, Buy
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
import string   
import random 
import re

def home(request):
    if "id" in request.session:
        id_per = int(request.session['id'])

        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else:
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        tt = False
        id_per = 2
        account = Account.objects.get(id=id_per)
    context = {'account': account, 'type': tt}
    return render(request, 'base/welcome.html', context)

def projects_pricol(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])

        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else:
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        id_per = 2
        tt = False
        account = Account.objects.get(id=id_per)
    p = True
    s = request.GET.get('s', '')  # Достаточно использовать второй аргумент для значения по умолчанию
    q = request.GET.get('q', '')

    # Экранирование специальных символов для регулярных выражений
    s_escaped = re.escape(s)
    creator = Account.objects.get(login=pk)
    projectsf = creator.project_set.all()
    print(projectsf)
    projects = projectsf.filter(Q(name__icontains=s) | Q(description__icontains=s))
    projects = projects.filter(Q(kvantum__icontains=q))
    name = creator.name
    context = {'projects': projects, 'account': account, 'home': p, 'type': tt, "name": name}
    return render(request, 'base/home.html', context)


def projects(request):
    if "id" in request.session:
        id_per = int(request.session['id'])

        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else:
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        id_per = 2
        tt = False
        account = Account.objects.get(id=id_per)
    p = True
    s = request.GET.get('s', '')  # Достаточно использовать второй аргумент для значения по умолчанию
    q = request.GET.get('q', '')
    name = "Проекты"
    # Экранирование специальных символов для регулярных выражений
    s_escaped = re.escape(s)

    projects = Project.objects.filter(Q(name__icontains=s) | Q(description__icontains=s))
    projects = projects.filter(Q(kvantum__icontains=q))

    context = {'projects': projects, 'account': account, 'home': p, 'type': tt, "name": name}
    return render(request, 'base/home.html', context)


def buy(request, pk):

    if "id" in request.session:
        type_acc = request.session['type']
        id_per = int(request.session['id'])
        if type_acc=="teacher":
            tt = True
            return redirect(f'/teacher/{id_per}')   
        else: 
            tt = False
            account = Account.objects.get(id=id_per)
        
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
            'account': account,
            'type': tt}
    return render(request, 'base/buy.html', context)


def project(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else: 
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        tt = False
        id_per = 2
        account = Account.objects.get(id=id_per)
    project = Project.objects.get(id=pk)
    coun = project.comments.count()
    images = Image.objects.all()
    context = {'project': project,
               'images': images,
               'account': account, 
               'type': tt, 
               'coun': coun}
    return render(request, 'base/project.html', context)



def account(request, pk):
    d = request.session.get('id')
    type_acc = request.session['type']
    if type_acc=="teacher":
            tt = True
    else: 
        tt = False
    d = "/" + str(d) + "/"
    if d in str(request.path):
        account = Account.objects.get(id=pk)
        account_ws = Account.objects.all()
        group = Group.objects.all()
        group = account.group_set.all()
        buys = Buy.objects.get(name=account.name)
        score = 0
        id_num = []
        rank_num = []
        for i in account_ws:
            id_num.append(i.id)
            rank_num.append(i.rank)
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


        context = {'account': account, 'type': tt, 'group': group, "buy": buys}
        return render(request, 'base/account.html', context)

    else:
        return redirect('/login/')
        
        
        

def login(request):
    ty = False
    if 'id' in request.session:
        if 'type' in request.session:                
            type_acc = request.session['type']
            if type_acc=='pupil':   
                id_per = int(request.session['id'])
                return redirect(f'/account/{id_per}/')
            else:
                id_per = int(request.session['id'])
                return redirect(f'/teacher/{id_per}/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                usr_account = Account.objects.get(login=cd["login"])
                ty = False
            except Account.DoesNotExist:
                print("Error Account")
                try: 
                    usr_account = Teacher.objects.get(login=cd["login"])
                    ty = True
                except Teacher.DoesNotExist:
                    return redirect('/login/')
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                print(ty)
                if ty:
                    request.session['type'] = "teacher"
                    print("dsadsad")
                    response = redirect(f'/teacher/{id_usr}/')
                else:
                    request.session['type'] = "pupil"
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
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else: 
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        return redirect('/login/')
    
    rank  = Account.objects.all().order_by("-rank")
    context = {'person': rank, "account": account, 'type': tt}
    return render(request, 'base/rating.html', context)

def shop(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else: 
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        tt = False
        id_per = 2
        account = Account.objects.get(id=id_per)
    shop = Shop.objects.all().order_by("-price")
    context = {'account': account, "shop": shop, 'type': tt}
    return render(request, 'base/shop.html', context)




def competitions(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else: 
            tt = False
            account = Account.objects.get(id=id_per)
    else:
        tt = False
        id_per = 2
        account = Account.objects.get(id=id_per)
    q = request.GET.get('q', '')
    s = request.GET.get('s', '')

    # Использование icontains для простого поиска без учета регистра
    competitions = Competitions.objects.filter(
        Q(name__icontains=q) | 
        Q(description__icontains=q) | 
        Q(kvantum__icontains=q)
    )

    # Если s не пусто, добавляем дополнительный фильтр
    if s:
        competitions = competitions.filter(Q(name__icontains=s))

    
    print(request.path)
    p = True
    context = {'competitions': competitions, 'account': account, 'competition': p, 'type': tt}
    return render(request, 'base/competitions.html', context)


def liked(request):
    if 'id' in request.session:
        id_per = request.session['id']
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
            account = Teacher.objects.get(id=id_per)
        else: 
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
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
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
        type_acc = request.session['type']
        if type_acc=="teacher":
            tt = True
        print(type_acc)
        if type_acc=="teacher":
            teacher = Teacher.objects.get(id=id_per)
            group = Group.objects.all()
            group = teacher.group_set.all()
            context = {'account': teacher, 'group': group, 'type': tt}
            return render(request, 'base/teacher.html', context)
        else:
            return redirect(f'/account/{id_per}')
    else:
        return redirect('/login')


def addproject(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc == "teacher":
            teacher = Teacher.objects.get(id=id_per)
            tt = True
        else:
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
    return render(request, 'base/newproject.html', {'form': form,'account': teacher, 'type': tt})


def addaccount(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc == "teacher":
            teacher = Teacher.objects.get(id=id_per)
            tt =True
        else:
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
    return render(request, 'base/newaccount.html', {'form': form,'account': teacher, 'type': tt})

def points_change(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
        type_acc = request.session['type']
        if type_acc == "teacher":
            tt = True
        else:
            return redirect('/')
    if request.method == 'POST':
        student_id = request.POST.get('student_id', None)
        points = request.POST.get('points', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        login = request.POST.get('login', None)
        password = request.POST.get('password', None)
        account = Account.objects.get(id=student_id)
        account.rank = points
        account.name = name
        account.email = email
        account.login = login
        account.password = password
        account.save()
        return HttpResponse("<h1>Nice!</h1>")


def post_comment(request):
    user = None
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = Account.objects.get(id=user_id)
        if request.method == "POST":
            text = request.POST.get('text', None)
            index = int(request.POST.get('index', None))
            tmp = Comment(author=user, text=text,)
            tmp.save()
            account = Account.objects.get(id=index)
            v.comments.add(tmp)
            print("success!")
            coun = account.comments.count()
            usr = account.accounts.all()
            context = {'artwork': artwork, 'coun': coun, 'usr': usr, 'user':user}
            return render(request, "artwork_comments.html", context=context)
    else:
        return redirect("/login/")