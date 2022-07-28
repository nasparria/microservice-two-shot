import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

# Import models from hats_rest, here.
# from api.shoes_rest import models
# from shoes_rest.models import Something
from shoes_rest.models import BinVO

def getting_bins():
    url = requests.get("http://wardrobe-api:8000/api/bins/")
    response = requests.get(url)
    content = json.loads(response.content)
    for bin in content["bins"]:
        BinVO.objects.update_or_create(
            id=bin["id"],
            closet_name=bin["closet_name"],
            bin_number=bin["bin_number"],
            bin_size=bin["bin_size"],
        )

def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            # Write your polling logic, here
            getting_bins()
            pass
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(10)


if __name__ == "__main__":
    poll()
