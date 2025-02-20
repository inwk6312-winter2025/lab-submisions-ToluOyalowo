import yaml
import requests
from requests.auth import HTTPBasicAuth

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

restconf_url_template = "https://{management_ip}/restconf/data/ietf-interfaces:interfaces/interface/{interface_name}"

headers = {
            "Content-Type": "application/yang-data+json",
                "Accept": "application/yang-data+json"
}

username = 'student'
password = 'Meilab123'

def configure_interface(management_ip, interface_name, ip_address):
    url = restconf_url_template.format(management_ip=management_ip, interface_name=interface_name)
    data = {
        "ietf-interfaces:interface": {
            "name": interface_name,
            "type": "iana-if-type:ethernetCsmacd",
             "enabled": True,
             "ietf-ip:ipv4": {
                 "address": [
                     {
                         "ip": ip_address.split("/")[0],
                         "netmask": ip_address.split("/")[1]
                     }
                ]
            }
        }
    }

    response = requests.put(url, headers=headers, json=data, auth=HTTPBasicAuth(username, password), verify=False)

    if response.status_code == 201:
        print(f"Successfully configured {interface_name} on {management_ip} with IP {ip_address}")
    else:
        print(f"Failed to configure {interface_name} on {management_ip}: {response.text}")

with open("routers_conf.yml", "r") as file:
    config = yaml.safe_load(file)

for router, router_data in config["routers"].items():
    management_ip = router_data["management_ip"]
    for interface, ip_address in router_data["interfaces"].items():
        configure_interface(management_ip, interface, ip_address)
                                                            
