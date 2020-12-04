import psutil
import requests
import platform
import numpy as np
import json

class Monitor:
    def __init__(self, api_key='', host='http://localhost:5000') -> None:
        self.api_key = api_key
        self.host = host
        if self.auth():
            pass
        else:
            raise Exception('Not Authenticated Exception')

    def auth(self):
        auth_path = '/auth'
        data = dict()
        data['api_key'] = self.api_key
        res = requests.post(self.host + auth_path, json=data)
        if res.status_code == 200:
            return True
        else:
            print(res.status_code)
            False

    def get_cpu_usage(self, collect_second=5):
        cpu_usages = np.zeros(collect_second)
        for i in range(collect_second):
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_usages[i] = cpu_usage
        
        return cpu_usages.mean()

    def get_ram_usage(self):
        ram_usage = psutil.virtual_memory().percent

        return ram_usage

    def get_disk_memory(self):
        disk_memory = psutil.disk_usage('/').total
        return disk_memory

    def get_platform(self):
        operating_platform = platform.platform()
        return operating_platform

    def get_os(self):
        operating_system = platform.system()

        return operating_system

    def test(self):
        cpu_usage = self.get_cpu_usage(1)
        ram_usage = self.get_ram_usage()
        disk_memory = self.get_disk_memory()
        operating_system = self.get_os()
        operating_platform = self.get_platform()

        print(f'cpu_usage : {cpu_usage} ram_usage : {ram_usage}, disk_memory : {disk_memory}, os : {operating_system}, platform : {operating_platform}')
    
    def get_monitoring_info(self, collect_second=5):
        """
        모니터링할 데이터들을 수집하는 함수
        프로토타입에서는 CPU, RAM 사용량만을 수집
        """
        item = dict()
        cpu_usage = self.get_cpu_usage(1)
        ram_usage = psutil.virtual_memory().percent

        item['cpu_usage'] = cpu_usage
        item['ram_usage'] = ram_usage

        return item

    def get_server_info(self):
        """
        OS, CPU 정보 등 서버의 정보를 수집하는 함수
        프로토타입에서는 OS 정보만 수집
        """
        item = dict()

        disk_memory = self.get_disk_memory()
        operating_system = self.get_os()
        platform = self.get_platform()

        item['disk_memory'] = disk_memory
        item['os'] = operating_system
        item['platform'] = platform

        return item
    
    def make_request_form(self):
        """
        서버로 요청보낼 JSON 형태를 만들어 주는 함수
        """
        pass

    def send_monitoring(self):
        item = self.get_monitoring_info()
        url = self.host + '/' + 'monitoring'
        data = dict()
        data['api_key'] = self.api_key
        data['item'] = item
        print(data)
        # data_json = json.dumps(data)

        # Using the json parameter in the request will change the Content-Type in the header to application/json.
        res = requests.post(url, json=data)
        print(res.status_code)

class UbuntuMonitor(Monitor):
    """우분투 서버에 맞도록 오버라이딩 해서 구현
    Linux
    Args:
        Monitor ([type]): [description]
    """
    pass

class WindowsMonitor(Monitor):
    """윈도우 서버에 맞도록 오버라이딩 해서 구현
    Windows
    Args:
        Monitor ([type]): [description]
    """
    pass

class OSXMonitor(Monitor):
    """맥OS에 맞도록 오버라이딩 해서 구현
    Darwin

    Args:
        Monitor ([type]): [description]
    """
    pass

if __name__ == "__main__":
    m = Monitor()
    m.test()
    m.send_monitoring()