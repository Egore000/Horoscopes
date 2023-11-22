from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view()), # http://127.0.0.1:8000/horoscope/
    # path('Horoscopes/<slug: sign>/', Sign.as_view())
    path('Horoscope/<slug:sign>.html', prediction)
]