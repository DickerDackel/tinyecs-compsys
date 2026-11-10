from importlib import import_module
from pkgutil import iter_modules

from aenum import StrEnum


class Comp(StrEnum):
    ...


class Prop(StrEnum):
    ...


def register():
    """Register all tinyecs-compsys subpackages.

    Use this at the beginning of your project to import all immediate
    subpackages into the ``tinyecs.compsys`` namespace. Registered packages
    will inject their component IDs into ``tinyecs.compsys.Comp``.
    """

    for sub in iter_modules(__path__):
        if sub.ispkg:
            print(f'Importing {__name__}.{sub.name}')
            import_module(f'{__name__}.{sub.name}')
