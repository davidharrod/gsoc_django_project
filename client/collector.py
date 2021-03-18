#收集操作系统的名称、版本
#收集编译器的名称、版本
#收集主机。。。
import platform as pf

def getSysInfo():
    dic = {}
    dic['os'] = pf.platform()
    dic['compiler'] = pf.python_compiler()
    dic['cpuArch'] = pf.processor()
    return dic

# print(getSysInfo())


