# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl

webrepl.start()
gc.collect()

from app.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/hrysto97/esp-upython')
    o.install_update_if_available_after_boot('wifi-ssid', 'wifi-password')


def start():
    print('everything running fine')


def boot():
    download_and_install_update_if_available()
    start()


boot()
