from django.urls import path

from .api_views import api_list_shoes, api_list_bins, api_details_shoe

urlpatterns = [
    path(
        "shoes/", api_list_shoes, name="api_list_shoes"),
    path(
        "shoes/<int:pk>/", api_details_shoe, name="api_list_shoes"),
    # path("bins/", api_list_bins, name="api_list_bins"),
        # bin<int:bin_vo_encoder>/shoes_rest/",
        # api_list_shoes,
        # name="api_list_shoes",
    ]