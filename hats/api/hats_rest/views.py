from django.shortcuts import render
from .models import LocationVO, Hat
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from common.json import ModelEncoder
import json

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["style_name"]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
    ]


# class LocationVODetailEncoder(ModelEncoder):
#     model = LocationVO
#     properties = ["name", "import_href"]


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse({"hats": hats}, encoder=HatListEncoder,)
    else:
        content = json.loads(request.body)
        try:
            location = LocationVO.objects.get(id=content["location"])
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
