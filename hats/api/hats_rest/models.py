from django.db import models
from django.urls import reverse


class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True, null=True)
    closet_name = models.CharField(max_length=100, null=True)
    section_number = models.PositiveSmallIntegerField(null=True)
    shelf_number = models.PositiveSmallIntegerField(null=True)


class Hat(models.Model):
    fabric = models.CharField(max_length=200)
    style_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)
    location = models.ForeignKey(
        LocationVO,
        related_name="+",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # def __str__(self):
    #     return self.style_name

    # def get_api_url(self):
    #     return reverse("api_show_hats", kwargs={"pk": self.pk})
