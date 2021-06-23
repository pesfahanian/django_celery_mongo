from django.contrib import admin

from test_app.models import TestModel


class TestModelAdmin(admin.ModelAdmin):
    model = TestModel
    list_display = ['email', 'first_name', 'last_name', 'subject', 'message']
    list_filter = ['email', 'first_name', 'last_name', 'subject', 'message']
    search_fields = ['email']
    ordering = ['email']


admin.site.register(TestModel, TestModelAdmin)
