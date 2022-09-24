"""Market Data views."""
# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def overview(response):
    """View for overview page."""
    print(response)
    return HttpResponse("Index view.")
