from django.contrib import admin

from review.models import AppReview

# Register your models here.


@admin.register(AppReview)
class AppReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'date')
    search_fields = ['name']
    list_filter = ('name',)# because the list_filter must be tuple or list

    class Meta:
        model = AppReview


# admin.site.register(AppReview)
