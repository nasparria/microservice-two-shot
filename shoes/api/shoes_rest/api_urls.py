from django.urls import path

from .api_views import api_list_shoes

urlpatterns = [
    path(
        "shoes/", api_list_shoes, name="api_list_shoes",
        # bin<int:bin_vo_encoder>/shoes_rest/",
        # api_list_shoes,
        # name="api_list_shoes",
    ),
]