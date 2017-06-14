# wifi info
A Python library for getting wifi information.

## Installation

### Python 2.x

```bash
pip install wifiinfo
```

### Python 3.x

```bash
pip3 install wifiinfo
```


## Usage

```python
import wifiinfo

# Creates a wifi object
wifi = wifiinfo.getWifi('osx')
# Can add Operating System or it defaults to MacOSx

# Print out properties
wifi.printProperties()

'''
["agrCtlRSSI" -> "-54"]
["agrExtRSSI" -> "0"]
["agrCtlNoise" -> "-94"]
["agrExtNoise" -> "0"]
["state" -> "running"]
["op mode" -> "station"]
["lastTxRate" -> "450"]
["maxRate" -> "450"]
["lastAssocStatus" -> "0"]
["802.11 auth" -> "open"]
["link auth" -> "wpa2-psk"]
["BSSID" -> "90"]
["SSID" -> "YOUR_WIFI_NAME"]
["MCS" -> "24"]
["channel" -> "37,1"]
'''

# Get a single property
wifiName = wifi.get('SSID')
print (wifiName)
# wifiName would print:
# YOUR_WIFI_NAME
```



## Support Operating Systems and Versions

- MacOSx
- ~~Windows~~
- ~~Linux~~


### Tested On

- MacOSx Sierra - Version 10.12.4
