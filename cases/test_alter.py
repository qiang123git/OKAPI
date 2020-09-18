import os
import unittest
import ddt
from lib.utils import hash_code
from setting import DATA_PATH

@ddt.ddt
class Alter(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'AlterPassword.yaml'))
    def test_alter(self,**case):
        print(case)
        url=case.get('url')
        print(url)
        method=case.get('method')
        data=case.get('data')
        print(data)
        check=case.get('check')
        if 'old_password' in data:
            data['old_password']=hash_code(data['old_password'])
            print(data['old_password'])
        if 'new_password' in data:
            data['new_password'] = hash_code(data['new_password'])
            print(data['new_password'])
        try:
            if method.lower() == 'post':




if __name__ == '__main__':
    unittest.main()