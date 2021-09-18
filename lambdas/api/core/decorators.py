from .services import Service
from .services import SERVICES


def Injectable(services: List[type]=[]):
    """
    A class decorator used for injecting
    services as dependencies of a class.
    """
    def decorator(CLS):
        original_contructor = CLS.__init__
        def __init__(self, *args, **kwargs):
            for service in services:
                key = service.__name__
                self.setattr(key, SERVICES[key])
            original_contructor(self, *args, **kwargs)
        CLS.__init__ = __init__
        return CLS
    return decorator
