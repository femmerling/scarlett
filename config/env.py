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
        '8080')
    environ.setdefault(
        'SCARLETT_DEBUG',
        '1')
    environ.setdefault(
        'SCARLETT_DEFAULT_IMG',
        'https://s3-ap-southeast-1.amazonaws.com/prismapp-files/no-product-image.png')
