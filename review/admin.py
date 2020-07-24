from django.contrib import admin

from review.models import AppReview

# Register your models here.


@admin.register(AppReview)
class AppReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars')
    search_fields = ['name']

    class Meta:
        model = AppReview


# admin.site.register(AppReview)
