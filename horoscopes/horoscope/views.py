from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.views.generic import TemplateView

from datetime import datetime

from .models import Predictions
from .parser import get_data

class Home(TemplateView):
    template_name = 'horoscope/index.html'
    
    def get(self, request):
        date = datetime.now().strftime("%d.%m.%Y")
        ctx = {
            'date': date
        }
        return render(request, self.template_name, ctx)

def prediction(request, sign):
    date = datetime.now().strftime("%d.%m.%Y")
    data = Predictions.objects.all()
    ctx = {
        'date': date,
        'text': data.get(zodiak_sign = sign.lower()).content
    }
    return render(request, f"horoscope/Horoscope/{sign}.html", ctx)

def pageNotFound(request, exception):
    return render(request, "horoscope/PageNotFound.html")