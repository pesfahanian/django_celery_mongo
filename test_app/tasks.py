import logging

from time import sleep

from DCM.celery import app

# logger = logging.getLogger('DCM')
logger = logging.getLogger('mongo')


@app.task(name='test_app.execute_test_task')
def execute_test_task(metadata: dict) -> None:
    logger.info('Executing run test task...')

    logger.info(f'Metadata is: \n{metadata}')

    logger.info('Sleeping for 5s...')
    sleep(5)
    logger.info('Finished sleeping!')

    logger.info('Executing test task finished!')
