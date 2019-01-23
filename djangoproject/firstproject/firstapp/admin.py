from django.contrib import admin
from firstapp.models import Topic, WebPage, AccessRecord, CreditCard

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(CreditCard)
# Register your models here.
