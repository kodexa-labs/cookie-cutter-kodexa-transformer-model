"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

# Import the main functions and classes
# These imports will be resolved when the cookiecutter template is rendered
from .model import infer
from .transformer import Transformer