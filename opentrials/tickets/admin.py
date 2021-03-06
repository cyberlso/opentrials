# -*- coding: utf-8 -*-

from django.contrib import admin
from opentrials.tickets.models import *

class MediaInline(admin.StackedInline):
    model = Media

class FollowupInline(admin.StackedInline):
    model = Followup

class MediaAdmin(admin.ModelAdmin):
    list_display = ('file', )

class FollowupAdmin(admin.ModelAdmin):
    list_display = ('reported_by','subject','status','iteration_date', )
    list_display_links = ('subject', )
    inlines = [MediaInline]

    def save_model(self, request, instance, form, change):
        instance.reported_by = request.user
        super(FollowupAdmin, self).save_model(request, instance, form, change)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('created','context','creator')
    list_display_links = ('context',)
    search_fields = ('context',)
    inlines = [FollowupInline]

    def save_model(self, request, instance, form, change):
        instance.creator = request.user

        super(TicketAdmin, self).save_model(request, instance, form, change)

if Ticket not in admin.site._registry:
    admin.site.register(Ticket, TicketAdmin)

if Followup not in admin.site._registry:
    admin.site.register(Followup, FollowupAdmin)

if Media not in admin.site._registry:
    admin.site.register(Media, MediaAdmin)