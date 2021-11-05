from django.db import models


class Menu(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    category = models.CharField(max_length=32, null=False)
    name = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=256, null=False)
    is_sold = models.BooleanField(default=True)
    badge = models.CharField(max_length=16, default="NEW")

    class Meta:
        db_table = "menus"
