from restclient.orchestration.client import FMClient

conn = FMClient(url = "http://192.168.0.1:8787")
result = conn.get_controller_version()
print(result)
