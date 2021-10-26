from django.urls import path
from customers import views
# from .customers import views? 

# TODO: look into int:pk

urlpatterns = [
  path('customers/', views.customer_list),
  path('customers/<int:pk>/', views.customer_detail),
]
