import os
import ddt
import unittest
import requests
from setting import *
from lib.utils import *

@ddt.ddt
class AppKey(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'appkey为空修改密码.yaml'))
    def test_appkey(self,**case):
        print(case)
        url=case.get('url')
        method=case.get('method')
        data=case.get('data')
        check=case.get('check')
        if 'old_password' in data:
            data['old_password']=hash_code(data['old_password'])
            print(data['old_password'])
        if 'new_passworf' in data:
            data['new_password'] = hash_code(data['new_password'])
            print(data['new_password'])
        if method.lower() == 'post':
            res=requests.post(url,data=data)
            resp=res.text
            print(resp)
        else:
            res=requests.get(url,data=data)
            resp=res.text
            print(resp)
        result=set_res_data(resp)
        print(result)
        i=check[0]
        print(i)
        self.assertIn(i,result)

if __name__ == '__main__':
    unittest.main()


