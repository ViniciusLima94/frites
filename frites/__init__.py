"""
Frites
======

Framework of Information Theory for Electrophysiological data and Statistics
"""
import logging

from frites import io, mi, stats, utils, workflow  # noqa

# Set 'info' as the default logging level
logger = logging.getLogger('frites')
io.set_log_level('info')

__version__ = "0.0.0"
