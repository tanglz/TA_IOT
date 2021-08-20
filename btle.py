# Name: CC2650 SensorTag
# Alias: CC2650 SensorTag
# 98:07:2D:3F:E9:86
# Paired: yes
# Trusted: no
# Blocked: no
# Connected: yes
# LegacyPairing: no
# UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
# UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
# UUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)
# UUID: Battery Service           (0000180f-0000-1000-8000-00805f9b34fb)
# UUID: Unknown                   (0000ffe0-0000-1000-8000-00805f9b34fb)
# UUID: Vendor specific           (f000aa00-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000aa20-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000aa40-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000aa64-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000aa70-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000aa80-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000ac00-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000ccc0-0451-4000-b000-000000000000)
# UUID: Vendor specific           (f000ffc0-0451-4000-b000-000000000000)
# Modalias: bluetooth:v000Dp0000d0110

from gattlib import GATTRequester
device_mac_address = "98:07:2D:3F:E9:86"
req = GATTRequester(device_mac_address)
name = req.read_by_uuid("00002a00-0000-1000-8000-00805f9b34fb")[0]
print(name)
data = req.read_by_handle(0x21)[0]
print(data)
print("ok")

