from importlib import import_module
from importlib.resources import files

from aenum import StrEnum, auto


class Comp(StrEnum):
    NONE = auto()


class Prop(StrEnum):
    NONE = auto()


def register():
    """Register all tinyecs-compsy submodules.

    Use this at the beginning of your project to import all submodules into the ``tinyecs.compsys`` namespace.
    Registered modules will inject their components into ``tinyecs.compsys.Comp``.
    """

    BLACKLIST = ['__pycache__', '__init__.py']
    HOME = files()

    for sub in [_.name for _ in HOME.iterdir() if _.name not in BLACKLIST]:
        print(f'Importing {sub}')
        import_module(f'{__name__}.{sub}')
