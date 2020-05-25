from django.urls import path
from django.urls import include

from .views import indexView, get_festivals #get_places

urlpatterns = [
    path("", indexView, name="index"),
    path('<int:Destination_id>/', get_festivals, name='festivals')
    # path('<int:Destination_id>/', get_places, name='places')
]