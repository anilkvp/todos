"""

"""
from datetime import datetime

from celery import shared_task


@shared_task
def log_user_events(data):
    """

    """
    file_logger = FileLogger()
    file_logger.write(data)


class FileLogger:
    """

    """
    def __init__(self):
        """

        """
        self.log_file = '/home/eagleone/audit.log'

    def write(self, data):
        with open(self.log_file, '+a') as f:
            for k, v in data.items():
                t = datetime.now()
                f.write(f'{t} User update {k} - {v}\n')


if __name__ == '__main__':
    log_user_events({'Sample': 'Event'})
