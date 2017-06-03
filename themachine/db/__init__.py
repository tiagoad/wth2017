from mongoengine import connect
import os

connect(os.getenv('MONGO_DB'), host=os.getenv('MONGO_URL'))

def get_or_create(obj, **kwargs):
    try:
        return obj.objects.get(**kwargs)
    except obj.DoesNotExist:
        return obj(**kwargs)

