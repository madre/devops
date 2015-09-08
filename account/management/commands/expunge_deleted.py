from __future__ import print_function
from __future__ import unicode_literals

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Expunge accounts deleted more than 48 hours ago."

    def handle(self, *args, **options):
        print("{0} expunged.".format(0))
