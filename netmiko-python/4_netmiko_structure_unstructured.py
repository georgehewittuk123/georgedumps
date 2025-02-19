#!/home/george/Desktop/ansible-virtualenv/aci_ansible_learning_labs_code_samples/intro_module/venv/bin/python
# Use the virtual env interpreter
from netmiko import ConnectHandler  # Only import the ConnectHandler from netmiko - that's all we need
import json
import datetime
import traceback

if __name__ == "__main__":  # Ensures the script runs only when executed directly
    devices = [
        {
            "device_type": "cisco_ios",
            "host": "10.200.30.246",
            "username": "admin",
            "password": "admin",
            "secret": "admin",  # Enable password
        },
    ]

    for device in devices:
        try:
            netmiko_device = ConnectHandler(**device)  # Unpack each device dictionary
            netmiko_device.enable()  # Enter enable mode
            
            # Dynamically get the hostname from the device
            hostname = netmiko_device.find_prompt().strip("#>")  # Cleans the prompt output

            print(f"Connected to {hostname} ({device['host']})")

            # Run the command and parse the output
            output = netmiko_device.send_command('show ip int brief', use_textfsm=True)

            # Save output to a JSON file using the hostname
            with open(f"{hostname}_data.json", 'w') as file:
                json.dump(output, file, indent=4)

            netmiko_device.disconnect()

        except Exception as e:
            print(f"Failed to connect to {device['host']}: {str(e)}")
            traceback.print_exc()  # Print detailed error traceback
