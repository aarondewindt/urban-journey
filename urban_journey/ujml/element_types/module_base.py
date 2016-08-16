from dtst.dtsml.element_types.base import BaseDTSMLElement
from dtst.dtsml.element_types.input import InputElement


class ModuleBaseElement(BaseDTSMLElement):
    '''Base class for dtst modules. This base class implements the lxml specific API.'''

    def _init(self):
        super()._init()

    def _listener(self):
        pass

    def activate(self):
        pass

    def deactivate(self):
        pass

    def f(self):
        pass

    @staticmethod
    def lookup_child(document, element):
        # All child of module elements are module input elements.
        return InputElement
