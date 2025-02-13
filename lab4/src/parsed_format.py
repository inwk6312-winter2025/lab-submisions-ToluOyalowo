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

# Loop through each device in the devices list
for device in devices:
    try:
        
        net_connect = Netmiko(**device)
        output =  net_connect.send_command("show ip interface brief", use_textfsm=True)
        net_connect.disconnect()

        # Print the device's IP and its interfaces
        print(f"Interfaces for device {device['ip']}:")


        for interface in output:
            print(interface['interface'])

        print("-" * 50)  # Separator for readability

    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")
