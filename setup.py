import sys
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico', 'res/']

# TARGET
target = Executable(
    script="src/main/main.py",
    base="Win32GUI" if sys.platform == "win32" else None,
    target_name="PyOneDark.exe" if sys.platform == "win32" else "PyOneDark",
    shortcut_name="PyOneDark",
    shortcut_dir="DesktopFolder",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="PyOneDark",
    version="1.0.0.0",
    description="Modern GUI for Python applications",
    author="Wanderson M. Pimenta",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
