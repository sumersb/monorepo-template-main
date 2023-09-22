import json
from typing import Any


class BetterEncoder(json.JSONEncoder):
    """
    Child Class of JSONEncoder which allows you to convert complex numbers and ranges to JSON
    """
    def default(self, o: Any) -> Any:
        """
        takes in o and check if name is found in class otherwise passes it to parent class
        """
        name = type(o).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            super().default(o)
        encoded = encoder(o)
        encoded["__extended_json_type__"] = name
        return encoded

    def encode_complex(self, c):
        return {"real": c.real, "imag": c.imag}

    def encode_range(self, r):
        return {"start": r.start, "stop": r.stop, "step": r.step}


def dumps(obj, *args, **kwargs):
    """ 
    Allows obj to be passed in and converted to JSON 
    """
    return json.dumps(obj, cls=BetterEncoder, *args, **kwargs)


class BetterDecoder(json.JSONDecoder):
    """
    Child of JSONDecoder Takes in JSON object and is capable of converting complex and range objects as well
    """
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)

    def decode_complex(self, dic):
        return complex(dic["real"], dic["imag"])

    def decode_range(self, dic):
        return range(dic["start"], dic["stop"], dic["step"])


def loads(obj, *args, **kwargs):
    """ 
    Allows JSON obj to be passed in and converted to python objects including range and complex 
    """
    return json.loads(obj, cls=BetterDecoder, *args, **kwargs)
