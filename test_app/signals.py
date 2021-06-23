import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from test_app.models import TestModel
from test_app.tasks import execute_test_task

logger = logging.getLogger('DCM')


@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, created, **kwargs):
    if created:
        logger.info('Proceding to execute test task....')

        metadata = {
            'id': instance.id,
            'email': instance.email,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'subject': instance.subject,
            'message': instance.message
        }
        execute_test_task.delay(metadata=metadata)

        logger.info('Test task was successfully added to the queue!')
