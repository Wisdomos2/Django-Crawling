from django.urls import path, include
from . import views

app_name = 'lostarkCrawling'
urlpatterns = [

    path('save/', views.loaCrawlingView.as_view())
]
