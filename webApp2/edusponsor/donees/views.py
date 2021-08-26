from django.shortcuts import render
from .models import donee
from django.http import HttpResponse


def donee_list(request):
    doneess = donee.objects.all().order_by('date')
    return render(request, 'donees/donee_list.html', {'donees':doneess})

def donee_detail(request, slug):
    # return HttpResponse(slug)
    anyDonee = donee.objects.get(slug=slug)
    return render(request, 'donees/donee_detail.html', {'donee': anyDonee})