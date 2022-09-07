from django.contrib import admin

# Register your models here.

from .models import Account, Comments, Questions, Topics

@admin.register(Account)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email")
    
@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    list_display = ("id","topic", "date")
    
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("topic","question", "date")

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id","comment", "date")
    