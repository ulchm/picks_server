from django.contrib import admin
from .models import Pool, Pick


@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    list_display = ('pool', 'user', 'game', 'pick', 'is_locked')
    list_filter = ('is_locked',)