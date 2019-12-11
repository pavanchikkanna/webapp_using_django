from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    path('auth/',views.auth,name="auth"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('buy/',views.sale,name='buy'),
    path('profile/',views.profile,name='profile'),
    path('profileupdate/',views.profileupdate,name="profileupdate"),
    path('sell/',views.sell_form,name='sell'),
    path('upload/',views.upload,name='upload'),
    path('logout/',views.logout,name='logout'),
    path('want/',views.want,name='want')
]