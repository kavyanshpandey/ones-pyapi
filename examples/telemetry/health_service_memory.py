from restclient.telemetry.client import ONESClient 

conn  = ONESClient(url ='https://10.x.x.x', username="YOUR_USERNAME", password="YOUR_PASSWORD")

conn.connect()

print("HEALTH_SERVICES_MEMORY")
query_params = {
  "fromDate" : "2023-05-12 11:55:24",
  "toDate" : "2023-05-12 12:55:24",
  "deviceAddress" : "10.x.x.x"
}
print(conn.get_health_services_memory(query_params))