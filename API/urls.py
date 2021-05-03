from django.urls import path, include
from .import views

urlpatterns = [
    path('advisor/', views.AddAdvisor),
    path('register/', views.UserRegister),
    path('login/', views.UserLogin),
    path('<int:id>/advisor', views.AdvisorList),
    path('<int:userid>/advisor/<int:advisorid>/', views.BookAdvisor),
    path('<int:userid>/advisor/booking/', views.BookedAdvisorList),



]