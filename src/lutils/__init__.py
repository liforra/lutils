import warnings
import sys
from liforra_utils import *

warnings.warn(
    "Importing 'lutils' is deprecated and will be removed in a future version. "
    "Please use 'liforra_utils' instead.",
    DeprecationWarning,
    stacklevel=2
)

# Explicitly re-export everything from liforra_utils to this module's namespace
# This ensures that tools inspecting lutils see the same contents as liforra_utils
module = sys.modules[__name__]
source_module = sys.modules["liforra_utils"]

for name in dir(source_module):
    if not name.startswith("_"):
        setattr(module, name, getattr(source_module, name))
