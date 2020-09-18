"""
#!/usr/bin/python3.7.7
@Author:libo
@Time: 2020/9/17 22:59
@File:utils.py
@Software:PyCharm
@Project:OKAPI
"""
def set_res_data(res):
    if res:
        return res.lower().replace('":"','=').replace('":','=')
def set_res_data(resp):
    if resp:
        return resp.replace('":"','=').replace('":','=')
