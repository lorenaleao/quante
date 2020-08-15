import abc

class IObject(metaclass = abc.ABCMeta):
    @staticmethod
    @abc.abstractstaticmethod
    def convert(obj):
        raise NotImplementedError