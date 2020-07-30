from django import forms
from django.contrib import admin
from .models import WayPointType, BOMItem, WayPointSubType, WayPointBOM


class WayPointSubTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ('bom',)


class WayPointTypeAdmin(forms.ModelForm):
    class Meta:
        model = WayPointType
        fields = "__all__"


admin.site.register(WayPointType)
admin.site.register(BOMItem)
admin.site.register(WayPointBOM)
admin.site.register(WayPointSubType, WayPointSubTypeAdmin)
