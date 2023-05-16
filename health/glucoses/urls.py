from django.urls import path
from .views import glucoses_list, glucose_details


app_name = "glucoses"
urlpatterns = [
    path('', glucoses_list, name="list"),
    path('<bp_id>/', glucose_details, name="details"),
]
