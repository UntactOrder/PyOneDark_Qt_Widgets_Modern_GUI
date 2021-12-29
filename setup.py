import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','gui/','settings.json']

# TARGET
target = Executable(
    script="main.pyw",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "PyOneDark",
    version = "1.0.0.0",
    description = "Modern GUI for Python applications",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
