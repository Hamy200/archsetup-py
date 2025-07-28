from pathlib import Path
import importlib

BASE_PATH = Path("./")
HOME_TOCOPY = Path("./home/tocopy")
HOME = Path("/home/hc")

GIT_EMAIL="104378548+Hamy200@users.noreply.github.com"

class ModuleStore:
    def __init__(self, modules_dir, child_modules):
        self.modules_dir = modules_dir
        self.modules = self._init_modules(child_modules)

    def _init_modules(self, child_modules):
        imports = []
        for module in child_modules:
            imports.append(importlib.import_module(f"{self.modules_dir}.{module}"))

        return imports

