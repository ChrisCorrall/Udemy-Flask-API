# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:36:57 2019

@author: Chris
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
