import time
import machine, onewire, ds18x20
from app import secrets

from app.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/hrysto97/esp-upython', github_src_dir='app', main_dir='app', secrets_file='secrets.py')
    o.install_update_if_available_after_boot(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)


def print_temp():
    ds_pin = machine.Pin(4)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

    roms = ds_sensor.scan()
    print('Found DS devices: ', roms)

    while True:
        ds_sensor.convert_temp()
        time.sleep(1)
        for rom in roms:
            print(rom)
            print(ds_sensor.read_temp(rom))
        time.sleep(5)


def start():
    print_temp()


def boot():
    download_and_install_update_if_available()
    # start()
