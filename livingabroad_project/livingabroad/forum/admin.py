from django.contrib import admin

# Register your models here.

from .models import Account, Comments, Questions, Topics

@admin.register(Account)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email")
    
@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    list_display = ("id","slug","topic", "date")
    prepopulated_fields = {"slug": ("topic", )}
    
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("slug","topic","question", "date")
    prepopulated_fields = {"slug": ("question", )}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id","slug","topic","question","comment", "date")
    prepopulated_fields = {"slug": ("comment", )}