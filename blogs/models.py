from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    img = models.TextField()
    img2 = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    categorys = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    @property   
    def created_format(self):
        return self.created.strftime('%b %d %Y')