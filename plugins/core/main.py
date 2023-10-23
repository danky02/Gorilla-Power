from typing import Callable, Any
from gorilla import GorillaPlugin


types_formatter:dict[str, Callable[[Any], str]] = {
# NUMERIC TYPES
    # 'int'                       : lambda x: str(x),
    # 'float'                     : lambda x: str(x),
    # 'complex'                   : lambda x: str(x),
# BOOLEAN TIPES
    'bool'                      : lambda x: 'si' if x else 'no',
# SEQUENCE TYPES
    # 'list'                      : lambda x: str(x),
    # 'tuple'                     : lambda x: str(x),
    'range'                     : lambda x: str([_x for _x in x]),
# TEXT SEQUENCE TYPES
    'str'                       : lambda x: x,
# BINARY SEQUENCE TYPES
    # 'bytes'                     : lambda x: str(x),
    # 'bytearray'                 : lambda x: str(x),
    # 'memoryview'                : lambda x: str(x),
# SET TYPES
    # 'set'                       : lambda x: str(x),
    # 'frozenset'                 : lambda x: str(x),
# MAPPING TYPES
    # 'dict'                      : lambda x: str(x),
# CUSTOM TYPES
# PUT YOUR CUSTOM TYPES HERE
}



class Plugin(GorillaPlugin):
    name = "Core Simple Plugin"

    # PARSER OPTIONS
    suppress:bool = True
    copy_enable:bool = True
    paste_enable:bool = True
    
    def parser(self, text:str) -> str:
        eval_result = eval(text)
        type_name:str = type(eval_result).__name__

        if type_name in types_formatter:
            formatter = types_formatter[type_name]
            return formatter(eval_result)
        else:
            return eval_result