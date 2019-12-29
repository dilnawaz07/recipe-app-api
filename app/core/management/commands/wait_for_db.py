import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self,*args, **options):
        self.stdout.write('Waiting for db...')
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Db unavailable, waiting for 1 1sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB UP'))


