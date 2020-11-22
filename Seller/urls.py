from django.urls import path
from Seller import views

urlpatterns = [
    path('smenu',views.Seller_Menu,name='smenu'),
    path('slog',views.SLogin,name='slog'),
    path('valid',views.validate,name='valid'),
    path('sreg',views.Registration,name='sreg'),
    path('shome',views.SHome,name='shome'),
    path('add',views.Add,name='add'),
    path('adding',views.Adding,name='adding'),
    path('show',views.Display,name='show'),
    path('update',views.Update,name='update'),
    path('updatep',views.UpdateP,name='updatep'),
    # path('aquanty',views.AddQuanty,name='aquanty'),
    # path('dquanty',views.DQuanty,name='dquanty'),
    path('uquanty',views.Update_Quantity,name='uquanty'),
    path('delete',views.Delete,name='delete'),
    path('sord',views.Sorder,name='sord'),
    path('odetails',views.Order_Details,name='odetails'),
    path('cancel',views.Cancel,name='cancel'),
    path('statusupdate',views.Update_Order,name='statusupdate'),
    path('logout',views.logout,name='logout'),
]
