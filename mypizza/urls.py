from django.urls import path
from . import views
from .views import adminlogin, adminhomepage,authenticateadmin,deletepizza

urlpatterns = [
    path('authenticateadmin',views.authenticateadmin,name='authenticateadmin'),
    path('homepage',views.adminhomepage, name='adminhomepage'),
    path('adminlogout', views.logoutadmin, name='adminlogout'),
    path('addpizza',views.addpizza,name='addpizza'),
    path('deletepizza/<int:pizzaapk>', views.deletepizza, name='deletepizza'),
    path('', views.homepageview,name='homepageview'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('userloginview', views.userloginview, name='userloginview'),
    path('home',views.home,name='home'),
    path('authenticateuser',views.authenticateuser, name='authenticateuser'),
    path('userlogout',views.userlogout, name='userlogout'),
    path('placedorder',views.placedorder, name='placedorder'),
    path('adminlogin',views.adminlogin, name="adminlogin"),
    path('userorders', views.userorders, name='userorders'),
    path('adminorders',views.adminorders,name='adminorders'),
    path('acceptorder/<int:orderpk>',views.acceptorder,name='acceptorder'),
    path('declineorder/<int:orderpk>',views.declineorder,name='declineorder'),
]
