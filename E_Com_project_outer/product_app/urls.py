from django.urls import path
from product_app.views import pro_home, del_a, up_a

urlpatterns = [
    path('', pro_home, name = 'pro_home'), 
    path('del/<int:id>', del_a, name= 'delete'),
    path('update/<int:id>', up_a, name = 'update'),
]
