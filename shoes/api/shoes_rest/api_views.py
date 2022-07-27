from django.shortcuts import render
from django.http import JsonResponse

from .models import Shoe

from common.json import ModelEncoder

from django.views.decorators.http import require_http_methods

import json

# from events.models import Conference


# class ConferenceVODetailEncoder(ModelEncoder):
#     model = ConferenceVO
#     properties = ["name", "import_href"]


# class AttendeeListEncoder(ModelEncoder):
#     model = Attendee
#     properties = [
#         "name",
#     ]



@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_encoder=None):
    """
    Lists the attendees names and the link to the attendee
    for the specified conference id.

    Returns a dictionary with a single key "attendees" which
    is a list of attendee names and URLS. Each entry in the list
    is a dictionary that contains the name of the attendee and
    the link to the attendee's information.
    """
    if request.method == "GET":
        shoes = Shoe.objects.filter(bin=bin_vo_encoder)
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoesListEncoder,
            safe=False
        )
    # else:
    #     content = json.loads(request.body)

    #     # Get the Conference object and put it in the content dict
    #     try:
    #         conference = ConferenceVO.objects.get(id=conference_vo_id)
    #         content["conference"] = conference
    #     except ConferenceVO.DoesNotExist:
    #         return JsonResponse(
    #             {"message": "Invalid conference id"},
    #             status=400,
    #         )

    #     attendee = Attendee.objects.create(**content)
    #     return JsonResponse(
    #         attendee,
    #         encoder=AttendeeDetailEncoder,
    #         safe=False,
    #     )


class ShoesListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "name",
    ]