
# Filename: Bluetooth.py
# Timestamp: 07/31/2021 21:48:38
# Author: @iohgoodness
# Description: Will be connecting to bluetooth devices using python

# For reading eeg devices as well as potentially connecting to earbuds to give information

# Good article explaining helpful bluetooth python techniques: https://people.csail.mit.edu/albert/bluez-intro/index.html
# Another article discussing reverse enginnerring of Bluetooth https://reposhub.com/python/programming-with-hardware/brandonasuncion-Reverse-Engineering-Bluetooth-Protocols.html
# Connecting to bluetooth device via command line https://www.raspberrypi.org/forums/viewtopic.php?t=102273


# Going to purchase these headphones (Mini Wireless Bluetooth 4.1 Stereo Earphone In-ear Sports Headphones)
# Cheap walmart bluetooth 4.1 headphones

# NAME OF BLUETOOTH DEVICE 
# 
# YX-01
# 
# 


# BLUEZ TOTALLY LINUX SUPPORTED - WILL BE USING VMBOX WITH ALL CONNECTIONS

# simple inquiry example
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))