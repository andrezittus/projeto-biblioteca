from django.contrib import admin
from books import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'publisher', 'publication_year', 'edition', 'create_date', 'show')
    search_fields = ('title', 'author')
    list_per_page = 20
    list_max_show_all = 200
    list_editable = ('title','author','show')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',



