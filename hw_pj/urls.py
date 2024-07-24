from django.contrib import admin #Djangoの管理サイト（Admin Interface）を使うためのモジュール
from django.urls import path, include #DjangoのURLパターンを定義するためのpath関数 
from .views import hwfunction, hwClass, topPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', hwfunction),
    path('hw2/', hwClass.as_view()),
    path('top/', topPage.as_view()),
    path('', include('hwapp.urls'))
]
