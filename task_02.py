#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Performing standard access functions for list"""

import data

BALLETS = data.BALLETS      # getting data from 'data' module variable

del BALLETS[11]             # deleting item at 11th index

BALLETS[1] = 'Swan Lake'    # Changing value of second item of the list

BALLETS.append('Herman Schmerman')            # APPENDING

BALLETS.extend(['Don Quixote', 'Sylvia'])     # EXTENDING
