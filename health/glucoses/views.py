from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GlucoseForm
from .models import Glucose


@login_required
def glucoses_list(request):
    glucoses = Glucose.objects.filter(user=request.user)
    form = GlucoseForm()
    if request.method == "POST":
        form = GlucoseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('glucoses:list'))
    return render(request, "glucoses/list.html", {'glucoses': glucoses, 'form': form})


@login_required
def glucose_details(request, bp_id):
    glucose = Glucose.objects.get(user=request.user, id=bp_id)
    form = GlucoseForm(instance=glucose)
    if request.method == "POST":
        form = GlucoseForm(request.POST, instance=glucose)
        if form.is_valid():
            form.save()
    return render(request, "glucoses/details.html", {'glucose': glucose, 'form': form})