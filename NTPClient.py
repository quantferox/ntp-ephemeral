import ctypes
import ntplib
from datetime import datetime

r = ntplib.NTPClient().request("pool.ntp.org", version=3)

t = datetime.fromtimestamp(datetime.now().timestamp() + r.offset)


class ST(ctypes.Structure):
    _fields_ = [
        ("y", ctypes.c_ushort),
        ("m", ctypes.c_ushort),
        ("dow", ctypes.c_ushort),
        ("d", ctypes.c_ushort),
        ("h", ctypes.c_ushort),
        ("mi", ctypes.c_ushort),
        ("s", ctypes.c_ushort),
        ("ms", ctypes.c_ushort),
    ]


st = ST(
    t.year,
    t.month,
    0,
    t.day,
    t.hour,
    t.minute,
    t.second,
    t.microsecond // 1000,
)

result = ctypes.windll.kernel32.SetLocalTime(ctypes.byref(st))
print("Result:", result)
print("Error:", ctypes.GetLastError())
