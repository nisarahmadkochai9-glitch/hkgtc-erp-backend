from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    rate_to_base = models.DecimalField(max_digits=20, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
