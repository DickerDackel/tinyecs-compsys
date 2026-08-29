from importlib import import_module
from importlib.resources import files

from aenum import StrEnum, auto


class Comp(StrEnum):
    NONE = auto()


class Prop(StrEnum):
    NONE = auto()


def register():
    BLACKLIST = ['__pycache__', '__init__.py']
    HOME = files()

    for sub in [_.name for _ in HOME.iterdir() if _.name not in BLACKLIST]:
        print(f'Importing {sub}')
        import_module(f'{__name__}.{sub}')
