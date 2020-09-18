import os
import unittest

import ddt
import requests

from lib.utils import *

from setting import API_URL, BASE_PATH, DATA_PATH



@ddt.ddt
class LogoutAll(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'aogoutall.yaml'))
    def test_logouAll(self,**case):
        #构建参数
        # print(case)
        url=case.get('url')
        method=case.get('mathod')
        data=case.get('data')
        check=case.get('check')
        # print(check)


        res=requests.get(url,params=data)
        resp=res.text
        print(resp)
        print(type(resp))

        #构建的结果，匹配结果
        # check=['ret=200','err_code=0','"err_msg="']
        result = set_res_data(resp)
        for c in check:
            self.assertIn(c,result)

if __name__ == '__main__':
    unittest.main()