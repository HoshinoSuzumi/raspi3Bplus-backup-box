from pyudev import Context, Monitor

context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by('block')


def usbstate(cb):
    i = 0
    for device in iter(monitor.pool, None):
        if 'disk' in str(device['DEVTYPE']):
            i += 1
            c = i, device, device['DEVNAME'], device.find_parent('usb')
            cb(c)
