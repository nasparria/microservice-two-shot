from django.db import models
from django.urls import reverse
# from wardrobe.api.wardrobe_api.models import Bin


# class Bin(models.Model):
#     closet_name = models.CharField(max_length=100)
#     bin_number = models.PositiveSmallIntegerField()
#     bin_size = models.PositiveSmallIntegerField()

#     def get_api_url(self):
#         return reverse("api_bin", kwargs={"pk": self.pk})

#     def __str__(self):
#         return f"{self.closet_name} - {self.bin_number}/{self.bin_size}"

#     class Meta:
#         ordering = ("closet_name", "bin_number", "bin_size")

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
    bin = models.ForeignKey("BinVO", related_name="shoes",on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class BinVO(models.Model):
    # import_href = models.CharField(max_length=200, unique=True)
    closet_name= models.TextField()
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()

    def get_api_url(self):
        return reverse("api_details_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return self.closet_name








