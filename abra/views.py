from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import RcatdbItems

# Create your views here.

def index(request):
    return HttpResponse("category tree goes here")


def item(request, item_id):

   item = get_object_or_404(RcatdbItems, pk=item_id)

   return json_response(item.__dict__)
