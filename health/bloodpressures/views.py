from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BloodPressureForm
from .models import BloodPressure


@login_required
def bloodpressures_list(request):
    bloodpressures = BloodPressure.objects.filter(user=request.user)
    form = BloodPressureForm()
    if request.method == "POST":
        form = BloodPressureForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('bloodpressures:list'))
    return render(request, "bloodpressures/list.html", {'bloodpressures': bloodpressures, 'form': form})


@login_required
def bloodpressures_details(request, bp_id):
    bloodpressure = BloodPressure.objects.get(user=request.user, id=bp_id)
    form = BloodPressureForm(instance=bloodpressure)
    if request.method == "POST":
        form = BloodPressureForm(request.POST, instance=bloodpressure)
        if form.is_valid():
            form.save()

    return render(request, "bloodpressures/details.html", {'bloodpressure': bloodpressure, 'form': form})
