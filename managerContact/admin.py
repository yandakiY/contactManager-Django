from django.contrib import admin
from .models import Person , NumberTel

class NumberLine(admin.TabularInline):
    model = NumberTel
    extra = 3

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                ["name_person"]
            ),
        }),
        ("Date creation", {"fields": ['date_creation']})
    )
    
    inlines = [NumberLine]
    

# Register your models here.
admin.site.register(Person , PersonAdmin)