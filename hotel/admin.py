from django.contrib import admin
from hotel.models import Hotel, Room, Period
# Register your models here.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ['name', 'location']

    class Meta:
        model = Hotel

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        queryset = queryset.filter(administrator=request.user)
        return queryset

    def get_fields(self, request, obj=None):
        all_fields = super().get_fields(request, obj)

        if request.user.is_superuser:
            return all_fields

        all_fields.remove('administrator')
        return all_fields

    def save_model(self, request, obj, form, change):

        if not obj.pk:
            administrator = form.cleaned_data.get('administrator')

            if not administrator:
                obj.administrator = request.user

        super().save_model(request, obj, form, change)


class RoomTabularLine(admin.TabularInline):
    model = Period


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomTabularLine]
    list_display = ('hotel', 'name', 'room_type')
    search_fields = ['name']

    class Meta:
        model = Room

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        queryset = queryset.filter(hotel__in=request.user.proprietar.all())

        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'hotel':
                kwargs['queryset'] = Hotel.objects.filter(administrator=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)




