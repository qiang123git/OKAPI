import os   #引入os
API_URL='http://hn216.api.yesapi.cn/'  #小白接口登录url地址
APP_KEY='4F476813EC222132D61351A3AA1D159B'    #登录必填项APP_key
BASE_PATH=os.path.dirname(os.path.abspath(__file__))    #项目工程路径
DATA_PATH=os.path.join(BASE_PATH,'data')  #data下的用例路径
REPORT_PATH=os.path.join(BASE_PATH,'report')   #用于存放报告的路径，report存放测试结果报告