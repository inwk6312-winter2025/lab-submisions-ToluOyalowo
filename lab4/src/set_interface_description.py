from netmiko import Netmiko

# List of devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]


description = 'Description set with Netmiko'

description_config = [
    "interface Loopback0",  #
    f"description {description}",  
    "ip address 10.10.10.1 255.255.255.0",  
    "no shutdown"  
    ]

# Loop through each device
for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_config_set(description_config)
        print(f"Configuration output for device {device['ip']}:\n{output}")
        net_connect.disconnect()

    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")







