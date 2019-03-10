from pyudev import Context, Monitor
import os

context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by('block')


def usbstate(callback):
    usb = 0
    sdcard = 0
    for device in iter(monitor.poll, None):
        type = str(device['DEVTYPE'])
        sdcard = os.path.exists("")
        if type in 'disk':
            mountpath, block, state = device, device['DEVNAME'], device.action
            if "1-1.1.2" in str(mountpath) and "add" in str(state)and "/block/sd" in str(mountpath):
                os.system("sudo mkdir /media/pi/sd ;chmod 777 /media/pi/usb")
                os.system("sudo mount "+block+"1 /media/pi/sd")
                usb = block+"1"

            if "1-1.1.2" in str(mountpath) and "remove" in str(state)and "/block/sd" in str(mountpath):
                usb = 0
                os.system("sudo rm -rf /media/pi/usb")

            if "1-1.2" in str(mountpath) and "add" in str(state) and "/block/sd" in str(mountpath):
                os.system("sudo mkdir /media/pi/usb ;chmod 777 /media/pi/sd")
                os.system("sudo mount "+block+"1 /media/pi/sd")
                sdcard = block+"1"

            if "1-1.2" in str(mountpath) and "remve" in str(state) and "/block/sd" in str(mountpath):
                sdcard = 0
                os.system("sudo rm -rf /media/pi/sd")

            if sdcard != 0 and usb != 0:
                return usb, sdcard
