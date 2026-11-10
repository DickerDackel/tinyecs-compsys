# tinyecs-compsys

This is the namespace to contain all other `tinyecs-compsys-XXXX`
packages.

## Synopsis

``` python
import tinyecs.compsys as cs

cs.register()
```

## Usage

Besides finding and registering sub modules, this package has no direct
functionality. Calling the `register` function will import all
submodules, which will in turn inject all their components into the
`Comp` `aenum`.

## Installation

It\'s up to you, if you install the currently provided
[compsys]{.title-ref} packages from [tinyecs]{.title-ref} by using

``` console
pip install tinyecs[base]
```

or include them all by adding specific dependencies:

``` console
pip install tinyecs
pip install tinyecs-compsys
pip install tinyecs-compsys-base
```

## Support / Contributing

Issues can be opened on [github
issues](https://github.com/dickerdackel/tinyecs-compsys/issues)

## License

This software is provided under the MIT license.

See LICENSE file for details.
