from django.contrib import admin
from .models import Poll, Choice, Vote

# Register your models here.

admin.register(Poll)
admin.register(Choice)
admin.register(Vote)
