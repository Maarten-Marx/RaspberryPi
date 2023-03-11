import time
import RPi.GPIO as GPIO

motor_pins = range(4, 8)
trigger_pin = 17
echo_pin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

delay = .01


# noinspection DuplicatedCode
def measure_distance(trigger, echo):
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == GPIO.LOW:
        pass

    start_time = time.time()
    while GPIO.input(echo) == GPIO.HIGH:
        pass
    end_time = time.time()

    interval = end_time - start_time
    distance = interval * 17000
    return distance


while True:
    dis = measure_distance(trigger_pin, echo_pin)

    if dis > 30:
        print(f"Safe: {int(dis)}cm")
        time.sleep(.5)
    else:
        print(f"Alarm: {int(dis)}cm")
        while dis < 30:
            for idx, pin in enumerate(motor_pins):
                previous = motor_pins[idx - 1]
                GPIO.output(previous, GPIO.LOW)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(delay)

            dis = measure_distance(trigger_pin, echo_pin)
