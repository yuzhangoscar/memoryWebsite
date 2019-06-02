from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('task', 'studied_date', 'first_review_date')
	list_filter = ('task', 'studied_date')
	search_fields = ('task', 'studied_date')
	date_hierarchy = 'studied_date'
	ordering = ('task', 'studied_date')