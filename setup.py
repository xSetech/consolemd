"""
ConsoleMD parses markdown using CommonMark-py (implementation of the
CommonMarkdown spec) and then fully renders it to the console in true color.
"""

import importlib.util
from pathlib import Path
from setuptools import setup

base_dir = Path(__file__).parent
pkg_name = 'consolemd'

def pseudo_import(pkg_name):
    """
    Return a new module that contains the variables of pkg_name.__init__
    """
    init_path = base_dir / pkg_name / '__init__.py'

    # Remove imports and 'from foo import'
    with open(init_path, 'r') as file:
        lines = [line for line in file if not line.startswith(('import', 'from'))]

    code = ''.join(lines)
    spec = importlib.util.spec_from_loader(pkg_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(code, module.__dict__)
    return module

# Trying to make this setup.py as generic as possible
module = pseudo_import(pkg_name)

setup(
    name=pkg_name,
    packages=[pkg_name],

    install_requires=[
        'click',
        'pygments',
        'setproctitle',
        'commonmark',
    ],

    extras_require={
        'test': [
            'pytest>=4.3.1',
            'pytest-runner>=4.4',
            'pytest-console-scripts>=0.1.9',
        ],
    },

    entry_points='''
        [console_scripts]
        consolemd=consolemd.cli:cli
    ''',

    # Metadata for upload to PyPI
    description="ConsoleMD renders markdown to the console",
    long_description=__doc__,
    version=module.__version__,
    author=module.__author__,
    author_email=module.__author_email__,
    license=module.__license__,
    keywords="markdown console terminal".split(),
    url=module.__url__,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],

    data_files=[],
)
