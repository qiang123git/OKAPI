import hashlib

def hash_code(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
def set_res_data(res):
    if res:
        return res.lower().replace('":"','=').replace('":','=')