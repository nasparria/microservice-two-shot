from django.db import models
# Create your models here.

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
    picture_url = models.URLField(null=True)
    bin = models.ForeignKey(BinVO, related_name="binn",on_delete=models.PROTECT)



