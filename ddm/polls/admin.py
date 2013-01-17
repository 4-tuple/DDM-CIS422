from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
#('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)