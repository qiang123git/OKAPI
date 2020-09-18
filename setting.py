#服务配置
import os

API_URL='http://hn216.api.yesapi.cn/'
APP_KEY='4F476813EC222132D61351A3AA1D159B'

#设置目录的绝对路径
BASE_PATH=os.path.dirname(os.path.abspath(__file__))
DATA_PATH=os.path.join(BASE_PATH,'data')
CASE_PATH=os.path.join(BASE_PATH,'case')
REPORT_PATH=os.path.join(BASE_PATH,'report')
