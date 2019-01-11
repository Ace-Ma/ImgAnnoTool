"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ImgAnnoTool.py']
DATA_FILES = ['icons/']
OPTIONS = {
    'iconfile': 'icons/iconfile.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)