from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro, name="intro"),
    path("screen1", views.screen1, name="screen1"),
    path("screen2/", views.screen2, name="screen2"),
    path("screen3/", views.screen3, name="screen3"),
    path("screen4/", views.screen4, name="screen4"),
    path("screen5/", views.screen5, name="screen5"),
    path("screen6/", views.screen6, name="screen6"),
    path("screen7/", views.screen7, name="screen7"),
    path("screen8/", views.screen8, name="screen8"),
    path("screen9/", views.screen9, name="screen9"),
    path("screen10/", views.screen10, name="screen10"),
    path("screen11/", views.screen11, name="screen11"),
    path("screen12/", views.screen12, name="screen12"),
    path("screen13/", views.screen13, name="screen13"),
]
