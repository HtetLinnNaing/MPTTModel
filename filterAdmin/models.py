from django.db import models


class BOMItem(models.Model):
    bom_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

    class Meta:
        db_table = "BOMItem"
        verbose_name_plural = "BoM Items"

    def __str__(self):
        return self.bom_name


class WayPointType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "WayPointType"
        verbose_name_plural = "WayPoint Types"

    def __str__(self):
        return self.name


class WayPointSubType(models.Model):
    name = models.CharField(max_length=100)
    wp_type = models.ForeignKey(WayPointType, on_delete=models.CASCADE)
    bom = models.ManyToManyField(BOMItem, related_name='bom')

    class Meta:
        db_table = "WayPointSubType"
        verbose_name_plural = "WayPoint SubTypes"

    def __str__(self):
        return self.name


class WayPointBOM(models.Model):
    quantity = models.PositiveIntegerField()
    type = models.ForeignKey(WayPointSubType, on_delete=models.CASCADE)
    bom = models.ForeignKey(BOMItem, on_delete=models.CASCADE)

    class Meta:
        db_table = "WayPointBOM"
