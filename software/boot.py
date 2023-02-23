###########
# boot.py #
###########
import passes

def do_connect(ssid, pwd):
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())

#def do_connect():
#    import network
#    wlan = network.WLAN(network.STA_IF)
#    wlan.active(True)
#    if not wlan.isconnected():
#        print('connecting to network...')
#        wlan.connect('ssid', 'key')
#        while not wlan.isconnected():
#            pass
#    print('network config:', wlan.ifconfig())


# Attempt to connect to WiFi network
do_connect(passes.wifiID, passes.wifiPass)

import webrepl

webrepl.start()