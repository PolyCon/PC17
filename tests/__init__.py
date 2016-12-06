import os
__all__ = [mod.split(".")[0] for mod in os.listdir("tests") if mod != "__init__.py"]