#!/home/george/Desktop/ansible-virtualenv/aci_ansible_learning_labs_code_samples/intro_module/venv/bin/python
# Use the virtal env interpreter
from netmiko import ConnectHandler # Only import the Connecthandler from netmiko - that's all we need
from getpass import getpass
import datetime

if __name__ == "__main__": #if someone imports this code as a module it doesn't just run whatever is below here automatically. allows us to seperate code a little bit
    devices = [ #I've added multiple devices so a LIST of DICTIONARIES
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
                bconfig = netmiko_device.send_command('show running-config')

                # Open the file and append to preserve previous backup
                with open('backup_config.txt', 'a') as file:
                    file.write(f"\n# Backup for {device['host']}:\n")
                    file.write(bconfig)
                print(f"Disconnected from {device['host']}\n")
            except Exception as e:
                print(f"Failed to connect to {device['host']}: {str(e)}")
                # Optionally print the full traceback
                import traceback
                traceback.print_exc()