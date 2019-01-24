from .exceptions    import InfeasibleError  # noqa
from .parser        import Parser           # noqa
from .scheduler     import Scheduler        # noqa
from .processor     import Processor        # noqa
from .task          import Task             # noqa

import os
debug = os.environ.get('DEBUG', '').lower() in ['1', 'true', 'on']
