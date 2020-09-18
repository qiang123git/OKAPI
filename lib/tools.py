def str(resp):
    if resp:
        return resp.lower().replace('":"','=').replace('":','=')