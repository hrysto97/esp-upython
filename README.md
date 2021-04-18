# Building an IoT smart control system with esp and micropython.

```buildoutcfg
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 write_flash -fs 1MB -fm dout 0x0 /home/traceur/Downloads/esp8266-20191220-v1.12.bin
picocom /dev/ttyUSB0 -b 115200

>>> import webrepl_setup # Setup webrepl
```