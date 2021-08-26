from django.shortcuts import render
from .models import donee

def donee_list(request):
    donees = donee.objects.all().order_by('date');
    return render(request, 'donee/donee_list.html', { 'donees': donees})
