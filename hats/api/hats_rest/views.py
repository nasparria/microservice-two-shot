from django.shortcuts import render
from .models import LocationVO, Hat
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from common.json import ModelEncoder
import json



class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = ["closet_name", "section_number", "shelf_number", "id"]


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
        "id",
    ]
    encoders = {
        "location": LocationVOEncoder(),
    }
    

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
        "id",
    ]
    encoders = {
        "location": LocationVOEncoder(),
    }




@require_http_methods(["GET", "POST"])
def api_list_hats(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id == None:
            hats = Hat.objects.all()
        else:
            hats = Hat.objects.filter(location=location_vo_id)
        return JsonResponse({"hats": hats}, encoder=HatListEncoder, safe=False)
    else:
        content = json.loads(request.body)
        try:
            location = LocationVO.objects.get(id=location_vo_id)
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



# @require_http_methods(["GET"])
# def api_list_locations(request):
#     bin = LocationVO.objects.all()
#     return JsonResponse(
#         {"bins": bin},
#         encoder=LocationVOEncoder
#     )
