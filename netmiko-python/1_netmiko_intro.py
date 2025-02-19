#!/home/george/Desktop/ansible-virtualenv/aci_ansible_learning_labs_code_samples/intro_module/venv/bin/python
# Use the virtal env interpreter
from netmiko import ConnectHandler # Only import the Connecthandler from netmiko - that's all we need
from getpass import getpass

if __name__ == "__main__": #if someone imports this code don't run whatever is below here automatically. allows us to seperate code a little bit
    device_dict = {
        "device_type" :  "cisco_ios_telnet",
        "host" : "10.200.30.246",
        "username" : "admin",
        "password" : getpass(),
    }
    
    netmiko_device = ConnectHandler((**device_dict))
    print(netmiko_device.find_prompt())
    print(
            netmiko_device.send_command("show version | include Version")
    )
    print(dir(netmiko_device))
    netmiko_device.disconnect()


