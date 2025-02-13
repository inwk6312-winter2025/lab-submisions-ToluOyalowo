from netmiko import ConnectHandler

# Define the devices in the network topology (Switch + 3 Routers)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Iterate over each device in the list
for device in devices:
    try:
        # Establish connection to the device
        net_connect = ConnectHandler(**device)

        # Send the 'show interface description' command to get interface descriptions
        output = net_connect.send_command("show interface description")

        # Disconnect from the device
        net_connect.disconnect()

        # Print the interface descriptions
        print("-" * 100)
        print(f"Interface Descriptions for {device['ip']}:")
        print(output)
        print("-" * 100)
        
    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")

