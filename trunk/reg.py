# -*- coding: utf-8 -*-
import _winreg

r = _winreg.OpenKey(
    _winreg.HKEY_CURRENT_USER,
    "Software\Microsoft\Windows\CurrentVersion\Internet Settings",
    0, #默认值为0
    _winreg.KEY_WRITE #注意该地方的值，默认值为_winreg.KEY_READ
)

_winreg.SetValueEx(r, 'ProxyEnable', 0, _winreg.REG_DWORD, 1)
_winreg.SetValueEx(r, 'ProxyServer', 0, _winreg.REG_SZ, "127.0.0.1:8080")

raw_input("any key to exit")
