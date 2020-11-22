from django.shortcuts import render,redirect
from Seller.models import Product,Seller
from Customer.models import Cart,Orders,Customer
from django.contrib import messages
import datetime
import random
import string

# Create your views here.
def Menu(request):
    return render(request,"Home.html")

def Customer_Home(request):
    #Customer.objects.all().delete()
    #Seller.objects.all().delete()
    #Product.objects.all().delete()
    #Cart.objects.all().delete()
    #Orders.objects.all().delete()
    try:
        if request.session['user']:
            return render(request,'CHome.html')
        else:
            res = Customer.objects.all()
            return render(request,"Customer.html",{'data':res})
    except KeyError:
        res = Customer.objects.all()
        return render(request,"Customer.html",{'data':res})
    

def CRegistration(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Customer(Name=Name,Mobile=Mobile,Email=Email,Password=Password).save()
        messages.info(request,"Your Registraion is successfull")
        return redirect("creg")
    else:
        return render(request,"CReg.html")

def CLogin(request):
    try:
        if request.session['user']:
            return render(request,'CHome.html')
        else:
            return render(request,'CLogin.html')
    except KeyError:
        return render(request,'CLogin.html')
    #return render(request,'CLogin.html')

def Cvalidate(request):
    Email = request.POST['email']
    Password = request.POST['password']

    try:
        Customer.objects.get(Email=Email,Password=Password)

        #request.session['status'] = True
        
        request.session['user'] = Email
        #request.session.set_expiry(30)
        return render(request,'CHome.html')
    except:
        return redirect('clog')

def CHome(request):
    try:
        if request.session['user']:
            name = request.session['user']
            print(name)
            return render(request,"CHome.html",{'name':name})
        else:
            return render(request,'CLogin.html')
    except KeyError:
        return render(request,'CLogin.html')
    

def Products(request):
    try:
        if request.session['user']:
            res = Product.objects.all()
            return render(request,'Products.html',{'data':res})
        else:
            return render(request,'CLogin.html')

    except KeyError:
        return render(request,'CLogin.html')

    #res = Product.objects.all()
    #return render(request,'Products.html',{'data':res})

def Adding_Cart(request):
    Customer_Email = request.session['user']
    print(Customer_Email)
    p_no = request.POST["id"]
    Seller_Email = request.POST["selleremail"]
    Name = request.POST["name"]
    Price = int(request.POST["price"])
    Weight = int(request.POST["weight"])
    Weight1 = request.POST["weight1"]
    CImage = request.POST['image']
    Quantity = int(request.POST["quantity"])
    Sub_Total = Price * Quantity
    print(Sub_Total)

    if Cart.objects.filter(Customer_Email=Customer_Email).exists():
        if Cart.objects.filter(Pro_Id=p_no).exists():
                messages.info(request,'Product Already exist in Cart')
                return redirect('prod')
            
        else:
            res = Product.objects.filter(id=p_no)
            for i in res:
                qua = i.Quantity
                print(qua)
                if Quantity > qua:
                    messages.info(request,'Quantity Not Available')
                    return redirect('prod')

                #elif Quantity < qua:
                    #messages.info(request,'Quantity Not Available')
                    #return redirect('prod')
                else:
                    Cart(Customer_Email=Customer_Email,Seller_Email=Seller_Email,Pro_Id=p_no,Name=Name,
                        Price=Price,Weight=Weight,Weight1=Weight1,CImage=CImage,Quantity=Quantity,
                        Sub_Total=Sub_Total).save()
                    res = Product.objects.all()
                    return render(request,"Products.html",{"data":res})

    else:
        res = Product.objects.filter(Name=Name)
        for i in res:
            qua = i.Quantity
            print(qua)
            if Quantity > qua:
                messages.info(request,'Quantity Not Available')
                return redirect('prod')

            #elif Quantity < qua:
                #messages.info(request,'Quantity Not Availabel')
                #return redirect('prod')
            else:
                Cart(Customer_Email=Customer_Email,Seller_Email=Seller_Email,Pro_Id=p_no,Name=Name,
                        Price=Price,Weight=Weight,Weight1=Weight1,CImage=CImage,Quantity=Quantity,
                        Sub_Total=Sub_Total).save()
                res = Product.objects.all()
                return render(request,"Products.html",{"data":res})


def Show_Cart(request):
    Customer_Email = request.session['user']
    print(Customer_Email)
    
    if Cart.objects.filter(Customer_Email=Customer_Email).exists():
        Total = 0
        for item in Cart.objects.filter(Customer_Email=Customer_Email):
            Total += item.Sub_Total
            print(Total)
            New = Cart.objects.filter(Customer_Email=Customer_Email)
        return render(request,"Cart.html",{"car":New,'t':Total})
    else:
        messages.info(request,'Your Cart is Empty..Keep Shoping...')
        return render(request,"Cart.html")

def Add_Delete(request):
    Customer_Email = request.session['user']
    cid = request.POST.get('id')
    Pid = request.POST.get('pid')
    option = request.POST.get('op')
    q = int(request.POST.get('qua'))
    Price = request.POST.get('price')
    if option == '+':
        r = Product.objects.filter(id=Pid)
        for x in r:
            q2 = x.Quantity
            res = Cart.objects.filter(id=cid)
            for i in res:
                q1 = int(i.Quantity)
                p = int(i.Sub_Total)
                if q1 >= q2:
                    print(q1)
                    print(q2)
                    messages.info(request,'your already selected maximum Quantity')
                    return redirect('cart')
                else:
                    q1 = int(i.Quantity)
                    p = int(i.Sub_Total)
                    Quantity = q1 + q
                    Sub_Total = p + int(Price)
                    print(Quantity)
                    print(Sub_Total)
                    Cart.objects.filter(id=cid).update(Quantity=Quantity,Sub_Total=Sub_Total)
                    return redirect('cart')

    else:
        res = Cart.objects.filter(id=cid)
        for i in res:
            q1 = int(i.Quantity)
            p = int(i.Sub_Total)
            Quantity = q1 - q
            Sub_Total = p - int(Price)
            print(Quantity)
            print(Sub_Total)
            Cart.objects.filter(id=cid).update(Quantity=Quantity,Sub_Total=Sub_Total)
            return redirect('cart')

def Corders(request):
    Customer_Email = request.session['user']
    print(Customer_Email)

    res = Cart.objects.filter(Customer_Email=Customer_Email)
    for x in res:
        Customer_Email = x.Customer_Email
        Seller_Email = x.Seller_Email
        Pro_Id = x.Pro_Id
        Name = x.Name
        Price = x.Price
        Weight = x.Weight
        Weight1 = x.Weight1
        Quantity = x.Quantity
        Sub_Total = x.Sub_Total
        OImage = x.CImage

        print(Customer_Email)
        print(Seller_Email)
        print(Pro_Id)
        print(Name)
        print(Price)
        print(Weight)
        print(Weight1)
        print(Quantity)
        print(Sub_Total)
        print(OImage)

    res = Orders.objects.filter(Customer_Email=Customer_Email)
    return render(request,'Corders.html',{'ord':res})


def Check_Out(request):
    Customer_Email = request.session['user']
    print(Customer_Email)
    Total = request.POST["Total"]
    res = Cart.objects.filter(Customer_Email=Customer_Email)

    return render(request,"Check.html",{"car":res,"t":Total})

    #res = Cart.objects.filter(Customer_Email=Customer_Email)
    #for x in res:
            #Customer_Email = x.Customer_Email
            #Seller_Email = x.Seller_Email
            #Name = x.Name
            #Price = x.Price
            #Weight = x.Weight
            #Weight1 = x.Weight1
            #Quantity = x.Quantity
            #Sub_Total = x.Sub_Total
            #OImage = x.CImage

            #print(Customer_Email)
            #print(Seller_Email)
            #print(Name)
            #print(Price)
            #print(Weight)
            #print(Weight1)
            #print(Quantity)
            #print(Sub_Total)
            #print(OImage)

            #Orders(Customer_Email=Customer_Email,Seller_Email=Seller_Email,Name=Name,Price=Price,
                #Quantity=Quantity,Weight=Weight,Weight1=Weight1,Sub_Total=Sub_Total,OImage=OImage).save()

    #return redirect('cord')

def Place_Order(request):
    Customer_Email = request.session['user']
    print(Customer_Email)

    Payment_Mode = request.POST.get("Payment")

    res = Cart.objects.filter(Customer_Email=Customer_Email)
    for x in res:

        Customer_Email = x.Customer_Email
        Seller_Email = x.Seller_Email
        Pro_Id = x.Pro_Id
        Name = x.Name
        Price = x.Price
        Weight = x.Weight
        Weight1 = x.Weight1
        Quantity = x.Quantity
        Sub_Total = x.Sub_Total
        OImage = x.CImage

        print(Customer_Email)
        print(Seller_Email)
        print(Pro_Id)
        print(Name)
        print(Price)
        print(Weight)
        print(Weight1)
        print(Quantity)
        print(Sub_Total)
        print(OImage)

        Order_Status = 'Order Placed'
        print(Order_Status)

        def Oid():
            x = random.randrange(1000000000,9999999999)
            print(x)
            i = "OD"
            n = str(i)
            r = (n + str(x))
            num = str(r)
            print(num)
            try :
                order = Orders.objects.get(Order_Id=num)
                Oid()
            except Orders.DoesNotExist:
                return num
        Order_Id = Oid()
        Order_Date = datetime.datetime.today()
        #Order_Date = dt.strftime("%d-%m-%Y %H:%M:%S")
        print(Order_Date)

        Status_Date = datetime.datetime.today()
        print(Status_Date)
        
        Orders(Customer_Email=Customer_Email,Seller_Email=Seller_Email,Pro_Id=Pro_Id,Order_Id=Order_Id,
                Name=Name,Price=Price,Quantity=Quantity,Weight=Weight,Weight1=Weight1,Sub_Total=Sub_Total,
                OImage=OImage,Order_Status=Order_Status,Order_Date=Order_Date,Status_Date=Status_Date,
                Payment_Mode=Payment_Mode).save()

        res = Product.objects.filter(id=Pro_Id)
        for i in res:
            q = int(i.Quantity)
            print(q)
            qua = int(q) - int(Quantity)
            print(Quantity)
            print(qua)
            Product.objects.filter(id=Pro_Id).update(Quantity=qua)
            Cart.objects.all().delete()
    return redirect('cord')


def Order_Details(request):
    Customer_Email = request.session['user']
    Pid  = request.GET['Id']
    print(Pid)
    
    res = Orders.objects.filter(id=Pid)
    for x in res:
        Expected = x.Order_Date
        print(Expected)
        Expected_Date = Expected + datetime.timedelta(days=7)
        print(Expected_Date)
    return render(request,'OStatus.html',{'data':res,'Expected_Date':Expected_Date})

def Delete_Cart(request):
    Cid  = request.GET['Id']
    print(Cid)
    Cart.objects.filter(id=Cid).delete()
    return redirect('cart')


def Clogout(request):
    try:
        del request.session['user']
        return redirect('clog')
    except KeyError:
        return redirect('clog')