from django.db import models

class Term(models.Model):
    name = models.CharField(max_length = 100)
    defi = models.TextField()
    deck = models.CharField(max_length = 100, default='General')

    def __str__(self):
        return self.name


