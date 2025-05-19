from signal import pause
import time
from gpiozero import Device, LED


# Define LED and button
led = LED("GPIO18")
#button = Button(17)

# Toggle LED state on each button press
#button.when_pressed = led.toggle

while True:
    led.toggle
    print('toggle')
    time.sleep(1)

# Keep the script running
pause()
