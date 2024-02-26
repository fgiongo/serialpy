from pySerialTransfer import pySerialTransfer as txfer
import time


if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('/dev/ttyACM0')

        link.open()
        time.sleep(2)

        while True:
            size = link.available()
            if size:
                print(link.rx_obj(obj_type='f', start_pos=0))
                print(link.rx_obj(obj_type='f', start_pos=4))
                print(link.rx_obj(obj_type='f', start_pos=8))
                print(link.rx_obj(obj_type='f', start_pos=12))

    except KeyboadInterrupt:
            link.close()

