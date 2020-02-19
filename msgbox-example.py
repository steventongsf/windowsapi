import ctypes

user_handle = ctypes.WinDLL("user32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

hWnd = None
lpText = "Welcome from this Dialog Box"
lpCaption = "Dialog Box"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

error = k_handle.GetLastError()
if error != 0:
    print("Error code: {0}",format(error))
if response == 1:
    print("User clicked OK.")






