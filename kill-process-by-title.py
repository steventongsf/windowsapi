import ctypes

u_handle = ctypes.WinDLL("user32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

lpWindowName = ctypes.c_char_p(input("Enter window name to kill:").encode("utf-8"))

hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    print("Error Code: {0} - Failed getting handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Fetched handle")

lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
    print("Error Code: {0} - Failed getting handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Retrieved PID")

dwDesiredAccess = PROCESS_ALL_ACCESS

bInheritHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
if hProcess <= 0:
    print("Error Code: {0} - Failed getting handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Fetched handle")

uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:
    print("Error Code: {0} - Can't terminate process".format(k_handle.GetLastError()))
    exit(1)

exit(0)