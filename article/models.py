from django.db import models

# Create your models here.
# This class Article name will be commonly refered in Django Shell for
# operating database.
class Article(models.Model):
    #blog title
    title= models.CharField(max_length=100)
    category=models.CharField(max_length=50,blank=True)
    #auto_now_add设置True表示自动设置对象增加时间
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=True, null=True)

    # 其中__str__(self) 函数Article对象要怎么表示自己
    def __str__(self):
        return self.title

    # internal class Meta:
    # All the possible metadata options that you give your model in this class

    class Meta:
        # Options.ordering: The default ordering for the object
        # This is a tuple or list of strings. Each string is a field name
        # with an optional “-” prefix, which indicates descending order.
        # Fields without a leading “-” will be ordered ascending.
        # Use the string ”?” to order randomly.
        ordering=['-date_time']