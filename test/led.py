import inspect
import ctypes


class LED(object):
    def __init__(self, R, G, B, GND):
        self.R = R
        self.G = G
        self.B = B
        self.GND = GND

    def setState(self, state):
        pass

    def getState():
        pass

    def rmState():
        pass

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)

    def _async_raise(tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
