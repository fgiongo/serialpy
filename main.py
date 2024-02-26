from pySerialTransfer import pySerialTransfer as txfer
import time


def handleBNO08x():
    accel = []
    accel.append(link.rx_obj(obj_type='f', start_pos=0))
    accel.append(link.rx_obj(obj_type='f', start_pos=4))
    accel.append(link.rx_obj(obj_type='f', start_pos=8))

    gyro = []
    gyro.append(link.rx_obj(obj_type='f', start_pos=12))
    gyro.append(link.rx_obj(obj_type='f', start_pos=16))
    gyro.append(link.rx_obj(obj_type='f', start_pos=20))

    magnet = []
    magnet.append(link.rx_obj(obj_type='f', start_pos=24))
    magnet.append(link.rx_obj(obj_type='f', start_pos=28))
    magnet.append(link.rx_obj(obj_type='f', start_pos=32))

    linaccel = []
    linaccel.append(link.rx_obj(obj_type='f', start_pos=36))
    linaccel.append(link.rx_obj(obj_type='f', start_pos=40))
    linaccel.append(link.rx_obj(obj_type='f', start_pos=44))

    print('BNO08x:')
    print('accel')
    for i in accel:
        print(i)

    print('gyro')
    for i in gyro:
        print(i)

    print('magnet')
    for i in magnet:
        print(i)

    print('linaccel')
    for i in linaccel:
        print(i)

    return accel, gyro, magnet, linaccel

def handleBME688():
    temp = link.rx_obj(obj_type='f', start_pos=0)
    pressure = link.rx_obj(obj_type='f', start_pos=4)
    humidity = link.rx_obj(obj_type='f', start_pos=8)

    print('BME688:')
    print('temp:')
    print(temp)
    print('pressure:')
    print(pressure)
    print('humidity:')
    print(humidity)

    return temp, pressure, humidity


callback_list = [ handleBNO08x, handleBME688 ]


if __name__ == '__main__':
    try:

        link = txfer.SerialTransfer('/dev/ttyACM0', 9600)
        link.set_callbacks(callback_list)
        link.open()
        time.sleep(2)

        while True:
            link.tick()

    except KeyboadInterrupt:
            link.close()

