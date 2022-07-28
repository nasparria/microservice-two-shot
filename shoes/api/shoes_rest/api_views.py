from django.shortcuts import render
from django.http import JsonResponse

from .models import Shoe

from common.json import ModelEncoder

from django.views.decorators.http import require_http_methods

import json



@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse({"shoes": shoes}, encoder=ShoesListEncoder)
    else:
        contenido = json.loads(request.body)
        shoe = Shoe.objects.create(**contenido)
        return JsonResponse(
            shoe,
            encoder=ShoesListEncoder,
            safe=False,
        )
    




    # if request.method == "GET":
    #     shoes = Shoe.objects.filter(bin=bin_vo_encoder)
    #     return JsonResponse(
    #         {"shoes": shoes},
    #         encoder=ShoesListEncoder,
    #         safe=False
    #     )
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
        "manufacturer",
        "color",
        "picture_url",
        "binn",

    ]