from BAC0 import lite
import time
import dns.resolver


def display(elements):
    print(elements['properties']['presentValue'])


time.sleep(10)
bacnet = lite()
ips_list = dns.resolver.resolve(qname="bacnet_device_1", rdtype='A', search=None)
address = ips_list[0].address

bacnet.cov(address, ("analogInput", 4), callback=display, confirmed=False, lifetime=0)
bacnet.cov(address, ("analogInput", 1), callback=display, confirmed=False, lifetime=0)

while True:
    time.sleep(1)
