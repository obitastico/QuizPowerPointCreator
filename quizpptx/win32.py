import os
import sys


def LoadSystemModule(lib_dir, modname):
    # See if this is a debug build.
    import importlib.util
    import importlib.machinery
    suffix = '_d' if '_d.pyd' in importlib.machinery.EXTENSION_SUFFIXES else ''
    filename = "%s%d%d%s.dll" % \
               (modname, sys.version_info[0], sys.version_info[1], suffix)
    filename = os.path.join(lib_dir, "pywin32_system32", filename)
    loader = importlib.machinery.ExtensionFileLoader(modname, filename)
    spec = importlib.machinery.ModuleSpec(name=modname, loader=loader, origin=filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)


def import_win32():
    lib_dir = "C:\ProgramData\Anaconda3\Lib\site-packages"
    LoadSystemModule(lib_dir, "pywintypes")
    LoadSystemModule(lib_dir, "pythoncom")
