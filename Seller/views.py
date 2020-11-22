from django.shortcuts import render,redirect
from django.contrib import messages
from Seller.models import Product,Seller
from Customer.models import Orders
import datetime
from django.core.mail import send_mail

# Create your views here.
def Menu(request):
    return render(request,"Home.html")

def Seller_Menu(request):
    try:
        request.session['suser']
        return render(request,'SHome.html')

    except KeyError:
        res = Seller.objects.all()
        return render(request,"Seller.html",{'data':res})



#def Home(request):
    #try:
        #if request.session['user']:
            #return render(request,'FHome.html')
        #else:
            #return render(request,'Login.html')
    #except KeyError:
        #res = Seller.objects.all()
        #return render(request,"Home.html",{'data':res})
    #res = Farmer.objects.all()
    #return render(request,"Home.html",{'data':res})

def Registration(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Seller(Name=Name,Mobile=Mobile,Email=Email,Password=Password).save()
        messages.info(request,"Your Registraion is successfull")
        return redirect("sreg")
    else:
        return render(request,"Registration.html")

def SLogin(request):
    try:
        #request.session['user']
        #return render(request,'SHome.html')
        if request.session['suser']:
            return render(request,'SHome.html')
        else:
            return render(request,'Login.html')
    except KeyError:
        return render(request,'Login.html')
    #return render(request,'Login.html')

def validate(request):
    Email = request.POST['email']
    Password = request.POST['password']

    try:
        Seller.objects.get(Email=Email,Password=Password)

        #request.session['status'] = True
        
        request.session['suser'] = Email
        #request.session.set_expiry(30)
        return render(request,'SHome.html')
    except:
        return redirect('slog')

def SHome(request):
    name = request.session['suser']
    print(name)
    return render(request,"SHome.html")

def Add(request):
    name = request.session['suser']
    print(name)
    return render(request,'Add.html')

def Adding(request):
    Email = request.session['suser']
    print(Email)
    Name = request.POST['name']
    Price = request.POST['price']
    Quantity = request.POST['quantity']
    Weight = request.POST['weight']
    Weight1 = request.POST['weight1']
    PImage = request.FILES['image']

    Product(Email=Email,Name=Name,Price=Price,Quantity=Quantity,Weight=Weight,Weight1=Weight1,PImage=PImage).save()
    messages.info(request,'Product Added Successfully')
    return redirect('add')

def Display(request):
    Email = request.session['suser']
    print(Email)

    res = Product.objects.filter(Email=Email)
    for i in res:
        Email = i.Email
        Name = i.Name
        Price = i.Price
        Quantity = i.Quantity
        Weight = i.Weight
        Weight1 = i.Weight1

        print(Email)
        print(Name)
        print(Price)
        print(Quantity)
        print(Weight)
        print(Weight1)
        
    return render(request,'display.html',{'data':res})

def Update(request):
    Uid = request.GET['Id']
    res = Product.objects.get(id=Uid)
    return render(request,'Supdate.html',{'data':res})

def UpdateP(request):
    id = request.POST.get('uid')
    Name = request.POST.get('uname')
    Price = request.POST.get('uprice')
    Quantity = request.POST.get('uquantity')
    Weight = request.POST.get('uweight')
    Weight1 = request.POST.get('uweight1')

    Product.objects.filter(id=id).update(Name=Name,Price=Price,Quantity=Quantity,Weight=Weight,Weight1=Weight1)

    return redirect('show')

# def AddQuanty(request):
#     id = request.POST['id']
#     UQuan = request.POST['uquantity']
#     res = Product.objects.filter(id=id)
#     for x in res:
#         Qua = x.Quantity
#         print(Qua)

#         Quantity = int(UQuan) + int(Qua)

#         print(Quantity)
#         Product.objects.filter(id=id).update(Quantity=Quantity)
#         return redirect('show')

# def DQuanty(request):
#     id = request.POST['id']
#     UQuan = request.POST['uquantity']
#     res = Product.objects.filter(id=id)
#     for x in res:
#         Qua = x.Quantity
#         print(Qua)

#         Quantity =int(Qua) - int(UQuan)

#         print(Quantity)
#         Product.objects.filter(id=id).update(Quantity=Quantity)
#         return redirect('show')
def Update_Quantity(request):
    id = request.POST.get('id')
    option = request.POST.get('op')
    UQuan = int(request.POST.get('qua'))
    print(id)
    print(option)
    print(UQuan)
    print(type(UQuan))
    if option == '+':
        res = Product.objects.filter(id=id)
        for x in res:
            Qua = x.Quantity
            print(Qua)

            Quantity = int(UQuan) + int(Qua)

            print(Quantity)
            Product.objects.filter(id=id).update(Quantity=Quantity)
            return redirect('show')
        messages.info(request,'this is adding')
        return redirect('show')

    else:
        res = Product.objects.filter(id=id)
        for x in res:
            Qua = x.Quantity
            print(Qua)

            Quantity =int(Qua) - int(UQuan)

            print(Quantity)
            Product.objects.filter(id=id).update(Quantity=Quantity)
            return redirect('show')


def Delete(request):
    if request.method == 'POST':
        Did = request.POST.get('id')
        Product.objects.filter(id=Did).delete()
        return redirect('show')
    else:
        Did = request.GET['Id']
        Product.objects.filter(id=Did).delete()
        return redirect('show')



def Sorder(request):
    Email = request.session['suser']
    print(Email)
    try:
        res = Orders.objects.filter(Seller_Email=Email)
        #for x in res:
            #Pid = x.id
            #print(Pid)
            #data = Orders.objects.filter(id=Pid)
            #for i in data:
                #status = i.Order_Status
                #print(status)
        return render(request,'Sorders.html',{'data':res})
        #return render(request,'Sorders.html',{'data':res,'option':status})

    except:
        Orders.objects.filter(Seller_Email=Email)
        messages.info(request,'No orders are there')
        return render(request,'Sorders.html')

def Order_Details(request):
    pid = request.POST['id']
    res = Orders.objects.filter(id=pid)
    for x in res:
        Expected = x.Order_Date
        print(Expected)
        Expected_Date = Expected + datetime.timedelta(days=7)
        print(Expected_Date)
    return render(request,'Odetails.html',{'data':res,'Expected_Date':Expected_Date})


        
def Cancel(request):
    Pid = request.POST['id']
    Pro_Id = request.POST['pid']
    Quanty = request.POST['quantity']
    print(Pid)
    print(Pro_Id)
    print(Quanty)
    
    Status_Date = datetime.datetime.today()
    print(Status_Date)

    Order_Status = 'Order Cancelled'
    Orders.objects.filter(id=Pid).update(Order_Status=Order_Status,Status_Date=Status_Date)
    pro = Product.objects.filter(id=Pro_Id)
    print(Pid)
    for i in pro:
        qua = i.Quantity
        print(qua)
        Quantity = int(Quanty)+int(qua)
        print(Quantity)
        Product.objects.filter(id=Pro_Id).update(Quantity=Quantity)
        res = Orders.objects.filter(id=Pid)
        messages.info(request,'order status is updated')
        return render(request,'Odetails.html',{'data':res})


def Update_Order(request):
    Email = request.session['suser']
    print(Email)
    Pid = request.POST['id']
    option = request.POST['option']
    
    print(option)
    print(Pid)

    Status_Date = datetime.datetime.today()
    print(Status_Date)

    Expected_Date = datetime.date.today()+datetime.timedelta(days=7)
    print(Expected_Date)
    
    if option == 'select':
        messages.info(request,"please select an option")
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})

    elif option == 'Processing':
        Orders.objects.filter(id=Pid).update(Order_Status=option,Status_Date=Status_Date)
        messages.info(request,'order status is updated')
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})

    elif option == 'Shipping':
        Orders.objects.filter(id=Pid).update(Order_Status=option,Status_Date=Status_Date)
        messages.info(request,'order status is updated')
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})
    
    elif option == 'Shipped':
        Orders.objects.filter(id=Pid).update(Order_Status=option,Status_Date=Status_Date)
        messages.info(request,'order status is updated')
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})

    elif option == 'Out For Delivery':
        Orders.objects.filter(id=Pid).update(Order_Status=option,Status_Date=Status_Date)
        messages.info(request,'order status is updated')
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})

    elif option == 'Delivered':
        Orders.objects.filter(id=Pid).update(Order_Status=option,Status_Date=Status_Date)
        messages.info(request,'order status is updated')
        res = Orders.objects.filter(id=Pid)
        return render(request,'Odetails.html',{'data':res})
        
    else:
        res = Orders.objects.filter(id=Pid)
        for x in res:
            status = x.Order_Status
            if status == 'Order Placed':
                Expected_Date = datetime.date.today()+datetime.timedelta(days=7)
                print(Expected_Date)
                return render(request,'Odetails.html',{'data':res})


def logout(request):
    try:
        del request.session['suser']
        return redirect('slog')
    except KeyError:
        return redirect('slog')

