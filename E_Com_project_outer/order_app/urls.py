from django.urls import path
from order_app.views import ord_view

urlpatterns = [
    path('', ord_view, name = ord_view),
]
