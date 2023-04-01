import spidev
import time
import RPi.GPIO as GPIO

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


LED_A = 17
LED_B = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

led_a_val = GPIO.LOW
led_b_val = GPIO.LOW

while True:
    tmp0 = read_adc(0)
    tmp1 = read_adc(1)

    # Determine absolute difference between 2 potentiometers
    diff = abs(tmp0 - tmp1)

    print(f"Potentiometer 0: {tmp0}")
    print(f"Potentiometer 1: {tmp1}")

    # Change LED state only if difference is outside hysteresis gap
    # tolerance of 50
    if diff > 50:
        led_a_val = GPIO.HIGH if tmp0 > tmp1 else GPIO.LOW
        led_b_val = GPIO.LOW if tmp0 > tmp1 else GPIO.HIGH

    GPIO.output(LED_A, led_a_val)
    GPIO.output(LED_B, led_b_val)

    print(f"LED A: {'ON' if led_a_val == GPIO.HIGH else 'OFF'}")
    print(f"LED B: {'ON' if led_b_val == GPIO.HIGH else 'OFF'}")

    time.sleep(.5)
