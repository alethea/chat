# 9/23/2013
# Charles O. Goddard

from distutils.core import setup

setup(
    name='tinychat',
    version='0.0', 
    packages=['tinychat'],
    scripts=['scripts/tinychat-server.py',
             'scripts/tinychat-client.py']
)
