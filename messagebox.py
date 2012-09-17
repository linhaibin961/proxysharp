from ctypes import *

kernel32 = windll.kernel32

string1 = "test"
string2 = "test2"

#kernel32.MessageBox(None, string1, string2, MB_OK)
windll.user32.MessageBoxA(None, string1, string2, 1)
