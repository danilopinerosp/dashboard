"""Production dashboard views."""
# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def overview():
    """View for overview page."""
    return HttpResponse("Index view.")
