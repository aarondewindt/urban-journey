import builtins
from dtst.dtsml.attribute_types.base import AttributeBaseClass



class string_t(AttributeBaseClass):
    """
    String dtsml attribute descriptor.
    """
    def get(self, instance, owner):
        val_str = instance.get(self.attrib_name)
        if val_str is None:
            return self.get_optional(instance)
        else:
            return val_str

    def set(self, instance, x):
        instance.set(self.attrib_name, x)


class int_t(AttributeBaseClass):
    """
    Integer dtsml attribute descriptor.
    """
    def get(self, instance, owner):
        try:
            val_str = instance.get(self.attrib_name)
            if val_str is None:
                return self.get_optional(instance)
            else:
                return int(val_str)
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])

    def set(self, instance, x):
        try:
            instance.set(self.attrib_name, builtins.str(builtins.int(x)))
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])


class bool_t(AttributeBaseClass):
    """
    Boolean dtsml attribute descriptor.
    """
    def get(self, instance, owner):
        try:
            val_str = instance.get(self.attrib_name)
            if val_str is None:
                return self.get_optional(instance)
            else:
                return bool(val_str)
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])

    def set(self, instance, x):
        try:
            instance.set(self.attrib_name, builtins.str(builtins.bool(x)))
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])


class float_t(AttributeBaseClass):
    """
    Float dtsml attribute descriptor.
    """
    def get(self, instance, owner):
        try:
            val_str = instance.get(self.attrib_name)
            if val_str is None:
                return self.get_optional(instance)
            else:
                return float(val_str)
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])

    def set(self, instance, x):
        try:
            instance.set(self.attrib_name, builtins.str(builtins.float(x)))
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])


class list_t(AttributeBaseClass):
    """
    List dtsml attribute descriptor. The contents of the list are evaluated as python code.
    """
    def get(self, instance, owner):
        try:
            val_str = instance.get(self.attrib_name)
            if val_str is None:
                return self.get_optional(instance)
            else:
                return eval("[{}]".format(val_str))
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])

    def set(self, instance, x):
        try:
            instance.set(self.attrib_name, builtins.str(builtins.float(x)))
        except Exception as e:
            import sys
            raise type(e)(builtins.str(e) +
                          '\n    File {}, line {}'.format(instance.dtsml.filename,
                                                        instance.sourceline)).with_traceback(sys.exc_info()[2])