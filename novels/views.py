from django.http import HttpResponse
from django.template import loader
from .models import Author
from .models import Book

def novels(request):
  myauthor = Author.objects.all().values()
  mybook = Book.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'myauthor': myauthor,
    'mybook': mybook,
  }
  return HttpResponse(template.render(context, request))