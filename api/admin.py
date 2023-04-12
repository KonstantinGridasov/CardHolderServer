from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Card)
class GardAdmin(admin.ModelAdmin):
    class Meta:
        model = Card
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = '__all__'
