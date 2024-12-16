from BAC0 import lite
import time
import dns.resolver


time.sleep(10)
bacnet = lite()

ips_list = dns.resolver.resolve(qname="bacnet_device_1", rdtype='A', search=None)
address = ips_list[0].address

object_type = "analogInput"
object_instance = 4

result = bacnet.write(f"{address} {object_type} {object_instance} presentValue 1.43 - 8")
print(result)
