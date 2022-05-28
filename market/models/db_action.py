from django.db import models

from market.constants.constants import ActionStatusChoices


class DBAction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        choices=ActionStatusChoices.choices(),
        default=ActionStatusChoices.TODO.value,
        max_length=32,
    )
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
