from django.views import generic
from .models import Restaraunt
import json

class IndexView(generic.ListView):
    template_name = 'guide/index.html'
    model = Restaraunt
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        locations = []
        for restaraunt in Restaraunt.objects.all():
            loc = restaraunt.geometry['location']
            id_ = restaraunt.id
            name = restaraunt.name
            dat = [name, loc['lat'], loc['lng'], id_]
            locations.append(dat)
        context['locations'] = locations
        return context

class RestarauntDetail(generic.DetailView):
    template_name = 'guide/detail.html'
    model = Restaraunt
