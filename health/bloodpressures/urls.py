from django.urls import path
from .views import bloodpressures_list, bloodpressures_details


app_name = "bloodpressures"
urlpatterns = [
    path('', bloodpressures_list, name="list"),
    path('<bp_id>/', bloodpressures_details, name="details"),
]