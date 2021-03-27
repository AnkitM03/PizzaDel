from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PizzaModel, CustomerModel, OrderModel


# Create your views here.

def adminlogin(request):
    return render(request, "adminlogin.html")


def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.username=="user":
        login(request, user)
        return redirect('adminhomepage')

    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Username or Password")
        return redirect('adminlogin')


def adminhomepage(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    context = {
        'pizzas': PizzaModel.objects.all()
    }
    return render(request, 'adminhomepage.html', context)


def logoutadmin(request):
    logout(request)
    return redirect('adminlogin')


def addpizza(request):
    name = request.POST['pizza']
    price = request.POST['price']

    PizzaModel(name=name, price=price).save()

    return redirect('adminhomepage')


def deletepizza(request, pizzaapk):
    PizzaModel.objects.filter(id=pizzaapk).delete()
    return redirect('adminhomepage')


def homepageview(requeest):
    return render(requeest, 'homepageview.html')


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']

    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, "User already exist")
        return redirect('homepageview')



    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all()) - 1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id, phoneno=phoneno).save()
    messages.add_message(request, messages.ERROR, "User successfully created")
    return redirect('homepageview')



def userloginview(request):
    return render(request, 'userlogin.html')


def authenticateuser(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')

    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Username or Password")
        return redirect('userloginview')


def home(request):
    if not request.user.is_authenticated:
        return redirect('userloginview')
    username=request.user.username
    context={'username':username, 'pizzas': PizzaModel.objects.all()}
    return render(request,'customerwelcome.html', context)


def userlogout(request):
    logout(request)
    return redirect('userloginview')



def placedorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginview')
    username=request.user.username
    phoneno=CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address=request.POST['address']
    ordereditems=""
    for pizza in PizzaModel.objects.all():
        pizzaid=pizza.id
        name=pizza.name
        price=pizza.price
        quantity=request.POST.get(str(pizzaid)," ")
        if str(quantity)!="0" and str(quantity)!=" ":
            ordereditems=ordereditems+" Pizza: "+name+", Price: "+str(price)+", quantity: "+str(quantity)+", total = "+str(int(quantity)*int(price))

    print(ordereditems)
    OrderModel(username=username, phoneno=phoneno, address=address, ordereditems=ordereditems).save()
    messages.add_message(request, messages.ERROR,"Order placed Successfully")
    return redirect('home')


def userorders(request):
    orders=OrderModel.objects.filter(username=request.user.username)
    context={'orders' : orders}
    return render(request,'userorders.html',context)


def adminorders(request):
    orders=OrderModel.objects.all()
    context={'orders' : orders}
    return render(request,'adminorders.html',context)



def acceptorder(request,orderpk):
    order=OrderModel.objects.filter(id=orderpk)[0]
    order.status="Accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
