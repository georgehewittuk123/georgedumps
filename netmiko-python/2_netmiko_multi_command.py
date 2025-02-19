#!/home/george/Desktop/ansible-virtualenv/aci_ansible_learning_labs_code_samples/intro_module/venv/bin/python
# Use the virtal env interpreter
from netmiko import ConnectHandler # Only import the Connecthandler from netmiko - that's all we need
from getpass import getpass

if __name__ == "__main__": #if someone imports this code don't run whatever is below here automatically. allows us to seperate code a little bit
    devices = [ #I've added multiple devices so a LIST of DICTIONARIES
        {
            "device_type" :  "cisco_ios_telnet",
            "host" : "10.200.30.245",
            "username" : "admin",
            "password" : getpass(),
        },
        {
            "device_type" :  "cisco_ios_telnet",
            "host" : "10.200.30.246",
            "username" : "admin",
            "password" : getpass(),
        },
    ]

    for device in devices:
            try:
                netmiko_device = ConnectHandler(**device)  # Unpack each device dictionary
                print(f"Connected to {device['host']}")

                # Run the show inventory command
                print("I try to do a normal single command")
                print(netmiko_device.send_command("show inventory"))
                print("OK, i try multiple now in a loop")

                # List of commands to execute
                commands = ['show version', 'show ip route', 'show interfaces']
                for command in commands:
                    output = netmiko_device.send_command(command)
                    print(f"Output of '{command}':\n{output}")

                netmiko_device.disconnect()  # Disconnect after finishing the commands
                print(f"Disconnected from {device['host']}\n")
            except Exception as e:
                print(f"Failed to connect to {device['host']}: {str(e)}")
