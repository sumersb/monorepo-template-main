import json
from typing import Any


class BetterEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
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
    return json.dumps(obj, cls=BetterEncoder, *args, **kwargs)


class BetterDecoder(json.JSONDecoder):
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
    return json.loads(obj, cls=BetterDecoder, *args, **kwargs)
