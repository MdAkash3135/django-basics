from django.db import models




class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  pub_date = models.DateTimeField()
  rating = models.DecimalField(decimal_places=2, max_digits=4, default = 2.2)

  def __str__(self):
    return self.title
  
class Comment(models.Model):
  blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE,  related_name='comments')
  message = models.TextField()