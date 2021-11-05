from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    menu_id = models.ForeignKey("menus.Menu", related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=False)
    size = models.CharField(max_length=16, null=False)
    price = models.IntegerField(null=False)
    is_sold = models.BooleanField(default=True)

    class Meta:
        db_table = "items"
