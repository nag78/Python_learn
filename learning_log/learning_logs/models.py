from django.db import models

# Create your models here.
class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length= 200)
    date_add = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text

class Entry(models.Model):
    """Инфрмация изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'enteries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return str(self.text)[:50] + "..."
