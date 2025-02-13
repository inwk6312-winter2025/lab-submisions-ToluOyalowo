from netmiko import Netmiko

# List of devices in the network topology (Switch + 3 Routers)
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
        net_connect = Netmiko(**device)

        # Send 'show version' command to get the Configuration Register
        output = net_connect.send_command("show version")

        # Disconnect from the device
        net_connect.disconnect()

        # Find the Configuration Register in the output
        result = output.find("Configuration register is")
        if result != -1:
            # Extract the Configuration Register value from the output
            begin = result + len("Configuration register is") + 1  # Skip the string part
            end = output.find("\n", begin)  # Find the end of the line
            config_register = output[begin:end].strip()

            # Print the IP address and Configuration Register
            print(f"Device {device['ip']} => Configuration Register: {config_register}")
        else:
            print(f"Configuration Register not found for {device['ip']}")

    except Exception as e:
        print(f"Error connecting to {device['ip']}: {str(e)}")

