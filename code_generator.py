#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:09:47 2021

@author: ashish
"""

import base64


def generate():
    email=base64.b64decode("YW5hLmN1c3RvbWVyMTAwMEBnbWFpbC5jb20=").decode("utf-8")
    password=base64.b64decode("c29vbGVpbmNoYXJh").decode("utf-8")
    return [email,password]

