from django.contrib import admin
from .models import Author
from .models import Book

class NovelsAdmin1(admin.ModelAdmin):
  list_display = ("firstname", "lastname","phoneno")
  search_fields=Author.searchablefields
  
urlpatterns1 = [
    admin.site.register(Author, NovelsAdmin1)
]

class NovelsAdmin2(admin.ModelAdmin):
      list_display = ("bookname","year_of_publish")
      search_fields=Book.searchablefields
urlpatterns2 = [
    admin.site.register(Book, NovelsAdmin2)
 ]
