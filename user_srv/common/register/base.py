import abc

class BaseConsul(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def register(self, name, id, service_address, service_port, check=None):
        pass

    @abc.abstractclassmethod
    def deregister(sef, service_id):
        pass

    @abc.abstractclassmethod
    def get_all_service(self):
        pass

    @abc.abstractclassmethod
    def filter_service(self, service_id):
        pass
