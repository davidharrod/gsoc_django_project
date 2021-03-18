import json as js
from . collector import getSysInfo

def transferDicToJs():
    sys_info_dic = getSysInfo()
    sys_info_js = js.dumps(sys_info_dic,indent=4,
    separators=(',',':'))


