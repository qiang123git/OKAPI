import os
check = ['ret=200','err_code=0','"err_msg="','"msg=V3.1.0 YesApi App.User.OtherProfile"']
    for c in check:
        self.assertIn(c,check)
#设置目录的绝对路径
BASE_PATH=os.path.dirname(os.path.abspath(__file__))
#yaml测试用例存放位置
DATA_PATH=os.path.join(BASE_PATH,'data')
#unittest测试类文件存放位置
CASE_PATH=os.path.join(BASE_PATH,'cases')
#测试报告路径
REPORT_PATH=os.path.join(BASE_PATH,'report')



