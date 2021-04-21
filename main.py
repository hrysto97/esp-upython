import time
import machine, onewire, ds18x20
import secrets

import senko
import network


def connect_wlan(ssid, password):
    """Connects build-in WLAN interface to the network.
    Args:
        ssid: Service name of Wi-Fi network.
        password: Password for that Wi-Fi network.
    Returns:
        True for success, Exception otherwise.
    """
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass

    return True


def print_temp():
    ds_pin = machine.Pin(4)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

    roms = ds_sensor.scan()
    if roms:
        print('Found DS devices: ', roms)
    else:
        print('No devices found')
        return

    while True:
        ds_sensor.convert_temp()
        time.sleep(1)
        for rom in roms:
            print(rom)
            print(ds_sensor.read_temp(rom))


def start():
    pass
    # print_temp()


def boot():
    GITHUB_URL = "https://github.com/hrysto97/esp-upython/blob/main/"
    OTA = senko.Senko(url=GITHUB_URL, files=["main.py"])

    # Connect to Wi-Fi network.
    connect_wlan(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
