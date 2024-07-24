from django.urls import path #DjangoのURLパターンを定義するためのpath関数 
from .views import hwappview

urlpatterns = [
    path('hwapp/', hwappview)
]
