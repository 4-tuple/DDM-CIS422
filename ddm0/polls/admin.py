from polls.models import Poll
from django.contrib import admin #import http files to use for user interface
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
	

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Pin',              {'fields': ['pin']}),
        ('Date information', {'fields': ['fin_date']}),
    ]
	#it will check the option prt by calling chice inline object .
    inlines = [ChoiceInline]
    list_display = ('question','fin_date' , 'pin')
    list_filter = ['fin_date']
    search_fields = ['question']
    

admin.site.register(Poll, PollAdmin)
