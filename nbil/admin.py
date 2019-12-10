from django.contrib import admin

# Register your models here.
from .models import UR_conn, UR_objects

admin.site.register(UR_conn)
admin.site.register(UR_objects)

