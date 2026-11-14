from importlib import import_module
from pkgutil import iter_modules

from aenum import StrEnum


class Comp(StrEnum):
    ...


class Prop(StrEnum):
    ...


def register(star_import: bool = False) -> None:
    """Register all tinyecs-compsys subpackages.

    :param star_import: Do a star-import from all imported modules into the
        ``tinyecs.compsys`` namespace

    Use this at the beginning of your project to import all immediate
    subpackages into the ``tinyecs.compsys`` namespace. Registered packages
    will inject their component IDs into ``tinyecs.compsys.Comp``.

    .. note:: When using ``star_import=True``, this function will not care
    about name conflicts between different ``compsys`` libraries.  Later
    imports will override earlier ones.  Check each libraries documentation to
    see if you really want this.
    """

    for sub in iter_modules(__path__):
        if not sub.ispkg: continue

        print(f'Importing {__name__}.{sub.name}')
        pkg = import_module(f'{__name__}.{sub.name}')

        if star_import and hasattr(pkg, '__all__'):
            globals().update({name: getattr(pkg, name) for name in pkg.__all__})
