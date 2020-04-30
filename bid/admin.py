from django.contrib import admin
from .models import Bid,UserBid


class BidLineAdminInline(admin.TabularInline):
    model = Bid


class BidAdmin(admin.ModelAdmin):
    inlines = (BidLineAdminInline, )


admin.site.register(UserBid,BidAdmin)


