from django.urls import path
from . import views  

# . is nothing but the root directory of the project
app_name='Notes'


urlpatterns = [
    #mporting the response functions from the views file and addding it to the path
    path('',views.index,name="base_page" ),
    path('post/<str:slug>/',views.detail,name="Post_detail"),
    path('login/',views.login_response, name="Login_page"),
    path('signup/',views.signup_response,name="signup_page"),
    path('old_url/',views.old_url,name="old_url"),
    path('new_url',views.new_url_page,name="redirected_page"),
    path('home/', views.details_to_base,name="det_to_basepage"),
]

