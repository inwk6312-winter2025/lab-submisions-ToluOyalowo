from netmiko import Netmiko

# List of devices (3 routers)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]


for device in devices:
    try:
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show ip route", use_textfsm=True)
        net_connect.disconnect()
        print(f"Routing table for device {device['ip']}:")

        # Iterate over the parsed output and print the required fields
        for route in output:
            # Check if the required fields are in the route
            protocol = route.get('protocol', 'N/A')
            network = route.get('network', 'N/A')
            distance = route.get('distance', 'N/A')
            metric = route.get('metric', 'N/A')

        
            print(f"Protocol: {protocol}, Network: {network}, Distance: {distance}, Metric: {metric}")

        print("-" * 50)  # Separator for readability

    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")

