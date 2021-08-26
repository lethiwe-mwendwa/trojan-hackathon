from django.shortcuts import render
from .models import donee


def donee_list(request):
    doneess = donee.objects.all().order_by('date')
    return render(request, 'donees/donee_list.html', {'donees':doneess})
