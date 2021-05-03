from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import UserProfile,Books

class profileuser1(admin.ModelAdmin):
    list_display = ("user",)
class profileuser(admin.ModelAdmin):
    model=Books
    Inline=[profileuser1]
    list_display = ("user1","Title","Author","Genre")


admin.site.register(UserProfile,profileuser1)
admin.site.register(Books,profileuser)