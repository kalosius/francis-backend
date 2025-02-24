from django.contrib import admin
from . models import SeniorOne

# Register your models here.
admin.site.register(SeniorOne)


# Customize the admin site
admin.site.site_header = "ST.Francis School Admin"
admin.site.site_title = "ST.Francis Admin Portal"
admin.site.index_title = "Welcome to ST.Francis Administration"