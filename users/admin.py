# este recomandat sa le punem in ordine alfabetica
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from users.models import MyUser
# Register your models here.
# admin.site.register(MyUser)


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        exclude = [] #spune ce campuri nu vrem sa apara /acum le folosim pe toate
        # fields = ("email","password")


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        exclude = []


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name' )
    ordering = ('email',)
#
#
# admin.site.register(MyUser, MyUserAdmin)

# class MyUserAdmin(admin.ModelAdmin):
#     pass