from django.urls import path
from Customer import views

urlpatterns = [
    path('',views.Menu,name='menu'),
    path('cmenu',views.Customer_Home,name='cmenu'),
    path('clog',views.CLogin,name='clog'),
    path('creg',views.CRegistration,name='creg'),
    path('cvalid',views.Cvalidate,name='cvalid'),
    path('chome',views.CHome,name='chome'),
    path('prod',views.Products,name='prod'),
    path('addc',views.Adding_Cart,name='addc'),
    path('cart',views.Show_Cart,name='cart'),
    path('adquanty',views.Add_Delete,name='adquanty'),
    path('deletecart',views.Delete_Cart,name='deletecart'),
    path('cord',views.Corders,name='cord'),
    path('check',views.Check_Out,name='check'),
    path('placeorder',views.Place_Order,name='placeorder'),
    path('details',views.Order_Details,name='details'),
    path('clogout',views.Clogout,name='clogout'),
]
