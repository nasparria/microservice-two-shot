from django.urls import path
from .views import api_list_hats

urlpatterns = [
    # path("attendees/", api_list_attendees, name="api_create_attendees"),
    path(
        "hats/",
        api_list_hats,
        name="api_list_hats",
    ),
    # path("attendees/<int:pk>/", api_show_attendee, name="api_show_attendee"),
]
