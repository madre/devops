from __future__ import unicode_literals

from django.db import models


class EmailConfirmationManager(models.Manager):

    def delete_expired_confirmations(self):
        for confirmation in self.all():
            if confirmation.key_expired():
                confirmation.delete()
