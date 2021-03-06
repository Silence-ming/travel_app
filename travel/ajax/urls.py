from django.urls import path,include
from .views import *
urlpatterns = [
    path('ask/',ask),
    path('askDetail/',askDetail),
    path('askQuestion/',askQuestion),
    path('notes/',notes),
    path('note_detail/',note_detail),
    path('login/',login),
    path('reg/',reg),
    path('person/',person),
    path('cites/',cites),
    path('scenicBanners/',scenicBanners),
    path('firstScenic/',firstScenic),
    path('scenic/',scenic),
    path('scenicDetail/',scenicDetail),
    path('noteBanner/',noteBanner),
    path('asking/',asking),
    path('answer/',answer),
    path('writing',writing),
    path('collections/',collections),
    path('collect',collect),
    path('collectInfo/',collectInfo),
    path('MyTravel/',MyTravel),
    path('myAsks/',myAsks),
    path('myAnswers/',myAnswers),
    path('information/',information),
    path('update_info',update_info),
    path('rePassWord/',rePassWord),
    path('getScenices/',getScenices),
]