# from package_example.arithmetic_operators.operators import add


"""
if init file exists with below in the package_example dir
__init__.py
from .arithmetic_operators.operators import *

then in this file import statement can be written like this:
from package_example import add

else:
    from package_example.arithmetic_operators.operators import add
"""
from package_example import add

print(add(1,2))

"""
__init__.py file:
-----------------
1. The __init__.py file makes Python treat directories containing it as modules.
3. from Python 3.3, __init__.py is no longer required to define directories as importable Python packages.
2. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.
"""
