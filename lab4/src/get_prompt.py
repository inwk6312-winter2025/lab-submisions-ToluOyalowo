from netmiko import Netmiko

# Define the devices in the topology (Switch + 3 Routers)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
]

# Iterate over each device in the list and retrieve the prompt
for device in devices:
    try:
        # Establish the connection to the device
        net_connect = Netmiko(**device)
        
        # Print the default prompt of the device
        print(f"Default prompt for {device['ip']}: {net_connect.find_prompt()}")

        # Send 'disable' command and print the prompt
        net_connect.send_command_timing("disable")
        print(f"Prompt after 'disable' command on {device['ip']}: {net_connect.find_prompt()}")

        # Enter enable mode
        net_connect.enable()
        print(f"Prompt after 'enable' command on {device['ip']}: {net_connect.find_prompt()}")

        # Close the connection
        net_connect.disconnect()
    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")

