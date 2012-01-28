from celery.task import task

@task()
def process_images(photo):
    photo.processed_images()
