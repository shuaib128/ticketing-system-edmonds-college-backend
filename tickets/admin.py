from django.contrib import admin
from .models import (
    Organization, Subject, Ticket
)

admin.site.register(Organization)
admin.site.register(Subject)
admin.site.register(Ticket)