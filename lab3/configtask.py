from jinja2 import Template

# Jinja2 template
template_str = """hostname {{ hostname }}

interface Loopback0
 ip address 150.1.{{ router_id }}.{{ router_id }} 255.255.255.255

{% for intf in interfaces %}
interface {{ intf.name }}
 ip address {{ intf.ip }} {{ intf.mask }}
 no shutdown
{% endfor %}

router ospf 1
 router-id 150.1.{{ router_id }}.{{ router_id }}
{% for intf in interfaces %}
 network {{ intf.network }} {{ intf.wildcard }} area 0
{% endfor %}

end"""

# Define router data
routers = [
    {
        "hostname": "R1",
        "router_id": "1",
        "interfaces": [
            {"name": "GigabitEthernet1.12", "ip": "155.1.12.1", "mask": "255.255.255.0", "network": "155.1.12.0", "wildcard": "0.0.0.255"},
            {"name": "GigabitEthernet1.13", "ip": "155.1.13.1", "mask": "255.255.255.0", "network": "155.1.13.0", "wildcard": "0.0.0.255"},
            {"name": "GigabitEthernet1.14", "ip": "155.1.14.1", "mask": "255.255.255.0", "network": "155.1.14.0", "wildcard": "0.0.0.255"},
        ],
    },
    {
        "hostname": "R2",
        "router_id": "2",
        "interfaces": [
            {"name": "GigabitEthernet1.12", "ip": "155.1.12.2", "mask": "255.255.255.0", "network": "155.1.12.0", "wildcard": "0.0.0.255"},
        ],
    },
    {
        "hostname": "R3",
        "router_id": "3",
        "interfaces": [
            {"name": "GigabitEthernet1.13", "ip": "155.1.13.3", "mask": "255.255.255.0", "network": "155.1.13.0", "wildcard": "0.0.0.255"},
        ],
    },
    {
        "hostname": "R4",
        "router_id": "4",
        "interfaces": [
            {"name": "GigabitEthernet1.14", "ip": "155.1.14.4", "mask": "255.255.255.0", "network": "155.1.14.0", "wildcard": "0.0.0.255"},
        ],
    },
]

# Render configurations
template = Template(template_str)

for router in routers:
    config = template.render(router_id=router["router_id"], hostname=router["hostname"], interfaces=router["interfaces"])
    print(f"\n{'='*20} {router['hostname']} Configuration {'='*20}")
    print(config)

