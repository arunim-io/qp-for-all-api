from .main import *

if DEBUG:
    from .local import *
else:
    from .production import *
