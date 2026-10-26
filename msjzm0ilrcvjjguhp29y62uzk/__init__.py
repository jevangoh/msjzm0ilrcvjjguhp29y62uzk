from importlib.metadata import version, PackageNotFoundError
from .msjzm0ilrcvjjguhp29y62uzk import msjzm0ilrcvjjguhp29y62uzk as _

try:
    __version__ = version("msjzm0ilrcvjjguhp29y62uzk")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
