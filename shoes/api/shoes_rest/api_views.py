from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json

from common.json import ModelEncoder

from .models import Shoe, BinVO


class ShoesListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "name",
        "manufacturer",
        "color",
        "picture_url",
        "bin",
        "id",
    ]

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "bin_number",
        "bin_size",
        "id",
        "closet_name",
    ]

@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse({"shoes": shoes}, encoder=ShoesListEncoder, safe=False)
    else:
        contenido = json.loads(request.body)
        shoe = Shoe.objects.create(**contenido)
        return JsonResponse(
            shoe,
            encoder=ShoesListEncoder,
            safe=False,
        )
    
@require_http_methods(["GET"])
def api_list_bins(request):
    bin = BinVO.objects.all()
    return JsonResponse(
        {"bins": bin},
        encoder=BinVOEncoder
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

@require_http_methods(["DELETE"])
def api_details_shoe(request, pk):
    if request.method == "DELETE":
        cuenta, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({"Errased": cuenta > 0})