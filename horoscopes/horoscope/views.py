from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)

def prediction(request, sign):
    return render(request, f"./Horoscopes/{sign}.html")

def pageNotFound(request, exception):
    return render(request, "PageNotFound.html")