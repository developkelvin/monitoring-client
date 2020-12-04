
import platform
from monitor import *

def main():
    # check os
    # run by os
    pass


if __name__ == "__main__":
    server_os = platform.system()
    print(server_os)
    if server_os == "Windows":
        m = WindowsMonitor()
    elif server_os == 'Darwin':
        m = OSXMonitor()
    elif server_os == 'Linux':
        m = UbuntuMonitor()
    else:
        raise Exception('This Server is Not Pre-Defined OS')
    
    m.send_monitoring()
