#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


try:

    import readline

except ImportError:

    import pyreadline as readline

import rlcompleter

readline.parse_and_bind('tab: complete')