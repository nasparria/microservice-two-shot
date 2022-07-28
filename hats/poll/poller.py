import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()


from hats_rest.models import LocationVO


def get_locations():
    print("IS IT WORKING")
    url = "http://wardrobe-api:8000/api/locations/"
    response = requests.get(url)
    print("RESPONSE", response)
    content = json.loads(response.content)
    print("CONTENT", content)
    for location in content["locations"]:
        try:
            LocationVO.objects.update_or_create(
                import_href=location["href"],
                defaults={
                    # "id": location["id"],
                    "closet_name": location["closet_name"],
                    "section_number": location["section_number"],
                    "shelf_number": location["shelf_number"],
                },
            )
        except Exception as e:
            print("ERROR", e, file=sys.stderr)       
        print("SUCCESS", location)


def poll():
    while True:
        print('Hats poller polling for data')
        try:
            get_locations()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()