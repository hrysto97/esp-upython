import time

from app import secrets

from app.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/hrysto97/esp-upython', github_src_dir='app', main_dir='app', secrets_file='secrets.py')
    o.install_update_if_available_after_boot(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)


def start():
    while True:
        time.sleep(1)
        print('running...')


def boot():
    download_and_install_update_if_available()
    start()
