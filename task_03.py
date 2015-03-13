#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Performing standard access functions for tuples"""

import data

DIRECTIONS = data.DIRECTIONS      # getting data from 'data' module variable

# Getting length of tuple and replacing last item

DIRECTIONS = DIRECTIONS[:(len(DIRECTIONS)-1)] + ('West',)
