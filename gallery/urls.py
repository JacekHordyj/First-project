from django.urls import path
from . import views
# ####: 8000/other

urlpatterns = [
    path('',views.index, name = 'index'),
    path('my_view',views.my_view,name='my_view'),
    path('signup/',views.SignUpView.as_view(),name = 'signup'),
    path('login/',views.loginPage,name='login'),
    path('logged_out/',views.logged_outPage,name='logout'),
    path('home/',views.home_view,name='home'),
    path('new/',views.new_view,name='new')
]