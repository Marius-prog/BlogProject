from django.urls import path
# from . import views
from .views import HomeView

urlpatterns = [
    # path('', views.hello, name="hello"),
    path ('', HomeView.as_view(), name ='main'),
]
