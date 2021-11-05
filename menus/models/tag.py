from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    menu_id = models.ForeignKey("menus.Menu", related_name="tags", on_delete=models.CASCADE, db_column="menu_id")
    type = models.CharField(max_length=32, null=False)
    name = models.CharField(max_length=32, null=False)

    class Meta:
        db_table = "tags"
