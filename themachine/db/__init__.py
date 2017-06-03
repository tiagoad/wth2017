from mongoengine import connect
import os

connect(os.getenv('MONGO_DB'), host=os.getenv('MONGO_URL'))

def get_or_create(obj, **kwargs):
    """
    Gets an object or creates it

    :param obj:     Document object
    :param kwargs:  Arguments to pass to the object __init__

    :return:        Database-bound object
    """
    try:
        return obj.objects.get(**kwargs)
    except obj.DoesNotExist:
        return obj(**kwargs)

