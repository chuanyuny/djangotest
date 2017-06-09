from django.contrib import admin
from sign.models import Event,Guest

class EventAdmin(admin.ModelAdmin):
	list_display=['id','name','status','address','start_time','jiabin_sum','has_signed','has_not_signed']
	search_fields=['name']
	list_filter=['status']

class GuestAdmin(admin.ModelAdmin):
	list_display=['realname','phone','email','sign','create_time','event']
	search_fields=['realname','phone']
	list_filter=['sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)