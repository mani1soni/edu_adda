
import shutil
import psutil




def diskcheck():
       diskCheck = shutil.disk_usage('/')
       used = (diskCheck.free / diskCheck.total)*100
       print(used)
       return used>70

def cpu_Usage():
       cpu = psutil.cpu_percent(0.1)
       print(cpu)
       return cpu>20


if not diskcheck or not cpu_Usage:
       print('error')

else:

       print('Everything is ok')   
