#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename: config/config.py

import os.path

""" Upload """
MIDDLE_WIDTH = 225
THUMB_SIZE = (75, 75)
ICON_WIDTH = 50
ICON_BIG_WIDTH = 160

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../static/upload")
ICONS_DIR = os.path.join(os.path.dirname(__file__), "../static/icons")

""" Pager """
MINI_PAGE_SIZE = 20
MAX_PAGE_SIZE = 5 * MINI_PAGE_SIZE

