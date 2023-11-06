from hal import hal_input_switch as switch
from hal import hal_led as led
import time

def switch_input():
    while True:
        x = switch.read_slide_switch()
        if x == 0:  # Check if the switch is in the right (0) position
            # Blink the LED at 10 Hz for 5 seconds
            led.set_output(0, 1)
            start_time = time.time()
            while time.time() - start_time < 5:  # Run for 5 seconds
                time.sleep(0.05)  # 10 Hz blinking
                led.set_output(0, 1)
                time.sleep(0.05)
                led.set_output(0, 0)
            # Turn off the LED after 5 seconds
            led.set_output(0, 0)
        else:
            # Blink the LED when the switch is in the left (1) position
            led.set_output(0, 1)
            time.sleep(0.2)
            led.set_output(0, 0)
            time.sleep(0.2)

def main():
    switch.init()
    led.init()
    switch_input()

if __name__ == "__main__":
    main()





