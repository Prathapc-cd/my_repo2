from django.db import models

class Author(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  phoneno=models.IntegerField(null=True)
  searchablefields=['firstname','lastname']
  
def __str__(self):
    return f"{self.firstname} {self.lastname} "

class Book(models.Model):
  bookname = models.CharField(max_length=50)
  year_of_publish=models.IntegerField(null=True)
  searchablefields=["bookname"]
  
  def __str__(self):
    return f"{self.bookname} {self.year_of_publish} "
