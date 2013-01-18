from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
		(None,               {'fields': ['question']}),
		('Date information', {'fields': ['pub_date']}),
	]
inlines = [ChoiceInline]
list_display = ('question', 'pub_date', 'was_published_recently')
list_filter = ['pub_date']
search_fields = ['question']
date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)