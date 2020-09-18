import os
API_URL = 'http://hn216.api.yesapi.cn/'
API_KEY = 'C934E82FEE5E64FC9035E3315BA667AC'

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
CASE_PATH=os.path.join(BASE_PATH,'case')
DATA_PATH=os.path.join(BASE_PATH,'data')
REPORT_PATH=os.path.join(BASE_PATH,'report')

def checked(self):
    check = ['ret=200','err_code=0','"err_msg="','"msg=V3.1.0 YesApi App.User.OtherProfile"']
    for c in check:
        self.assertIn(c,check)
