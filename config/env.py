"""
Environment Config
------------------
Please put all environment specific config key/values here
"""

from os import environ

def set_default_config():
    environ.setdefault(
        'SCARLETT_HOST',
        '0.0.0.0')
    environ.setdefault(
        'SCARLETT_PORT',
        '8000')
    environ.setdefault(
        'SCARLETT_DEBUG',
        '1')
    environ.setdefault(
        'SCARLETT_DEFAULT_IMG',
        'https://docs.prismapp.io/assets/images/prism-logo.png')
