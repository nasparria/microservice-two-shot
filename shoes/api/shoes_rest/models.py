from django.db import models
from django.urls import reverse
# from wardrobe.api.wardrobe_api.models import Bin

class BinVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    name= models.CharField(max_length=200)


class Shoe(models.Model):
    """
    The Status model provides a status to a Presentation, which
    can be SUBMITTED, APPROVED, or REJECTED.

    Status is a Value Object and, therefore, does not have a
    direct URL to view it.
    """
    manufacturer = models.TextField()
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)
    binn = models.ForeignKey(BinVO, related_name="shoes",on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} - {self.name}/{self.color}"

    def get_api_url(self):
        return reverse("api_show_shoe", kwargs={"pk": self.pk})





