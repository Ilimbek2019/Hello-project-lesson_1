from django.urls import path
#from pages_app.views import homeView

#from . import views

#from .views import homeView

from .views import homeView, aboutView



urlpatterns=[
    path('', homeView, name="home"),
    path('about/',aboutView, name="about")
]
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/about/