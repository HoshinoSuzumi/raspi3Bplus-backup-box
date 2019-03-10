from "../src/usbstate" import usbstate


def cb(c):
    for a in c:
        print(a)


usbstate(cb)
