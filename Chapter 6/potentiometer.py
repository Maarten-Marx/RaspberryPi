import spidev
import time


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


def read_adc(adc_num):
    if not 0 <= adc_num <= 7:
        return -1
    r = spi.xfer2([1, (8 + adc_num) << 4, 0])
    time.sleep(0.00005)
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


while True:
    tmp0 = read_adc(0)
    print("input 0: ", tmp0)
    time.sleep(0.2)
