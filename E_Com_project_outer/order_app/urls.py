from django.urls import path
from order_app.views import ord_view, ord_update, ord_card

urlpatterns = [
    path('', ord_view, name = 'ord_view'),
    path('update/<int:id>', ord_update, name = 'ord_update'),
    path('card/<int:id>', ord_card, name= 'ord_card')
]
