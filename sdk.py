import ctypes
import os




# Load DLLs
zkemsdk = ctypes.WinDLL("./zkemsdk.dll")
commpro = ctypes.WinDLL(os.path.abspath("./commpro.dll"))
comms = ctypes.WinDLL(os.path.abspath("./comms.dll"))
zkemkeeper = ctypes.WinDLL(os.path.abspath("./zkemkeeper.dll"))
tcpcomm = ctypes.WinDLL(os.path.abspath("./tcpcomm.dll"))

# Define Z_ReadRTLog function prototype
Z_ReadRTLog = zkemsdk.Z_ReadRTLog
Z_ReadRTLog.restype = ctypes.c_int

# Define Z_Connect_NET function prototype
Z_Connect_NET = zkemsdk.Z_Connect_NET
Z_Connect_NET.restype = ctypes.c_int
Z_Connect_NET.argtypes = [ctypes.c_char_p, ctypes.c_int]

# Define Z_GetDeviceInfo function prototype
Z_GetDeviceInfo = zkemsdk.Z_GetDeviceInfo
Z_GetDeviceInfo.restype = ctypes.c_int
Z_GetDeviceInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

# Connect to the device
address = b"192.168.2.201"  # Example IP address of the attendance device
port = 4370  # Example port number
result_connect = Z_Connect_NET(address, port)

# Check the connection result
if result_connect == 0:
    print("Connected to the device successfully.")
else:
    print("Failed to connect to the device.")

# Define the prototype of the EMBUDP_INIT function
EMBUDP_INIT = tcpcomm.EMBUDP_INIT
EMBUDP_INIT.restype = ctypes.c_int  # Return type is int
EMBUDP_INIT.argtypes = [ctypes.c_char_p, ctypes.c_int]  # Arguments: address (string), port (int)



# Initialize communication with the TCP device
address = b"192.168.2.201"  # Example IP address of the TCP device (change this to the actual IP address)
port = 4370  # Example port number (change this to the actual port number)
result_init = EMBUDP_INIT(address, port)
# Check the initialization result
if result_init == 0:
    print("Initialized communication with the TCP device successfully.")
else:
    print("Failed to initialize communication with the TCP device.")
#get device handle    
device_handle = ctypes.c_void_p(result_init) 
# Read the latest attendance logs
result_read_log = Z_ReadRTLog(device_handle)
if result_read_log == 1:
    print("Attendance data read successfully.")
else:
    print("Failed to read attendance data.")
