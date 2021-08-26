from django.shortcuts import render, redirect
from .models import donee
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms



def donee_list(request):
    doneess = donee.objects.all().order_by('date')
    return render(request, 'donees/donee_list.html', {'donees':doneess})


def donee_detail(request, slug):
    # return HttpResponse(slug)
    anyDonee = donee.objects.get(slug=slug)
    return render(request, 'donees/donee_detail.html', {'donee': anyDonee})


@login_required(login_url="/accounts/login/")
def donee_create(request):
    if request.method == 'POST':
        form = forms.CreateDonee(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('donees:list')
    else:
        form = forms.CreateDonee()
    return render(request, 'donees/donee_create.html', { 'form': form })
