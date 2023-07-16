import RPi.GPIO as GPIO
import time
import pygame

# GPIO pin for moisture sensor
moisture_sensor_pin = 17

# Moisture threshold for triggering sound
moisture_threshold = 500

# Sound file path
sound_file = 'sound.wav'

# Sound duration in seconds
sound_duration = 2

# Initialize GPIO and Pygame mixer
GPIO.setmode(GPIO.BCM)
GPIO.setup(moisture_sensor_pin, GPIO.IN)

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    time.sleep(sound_duration)
    pygame.mixer.music.stop()

try:
    while True:
        moisture_level = GPIO.input(moisture_sensor_pin)

        if moisture_level < moisture_threshold:
            play_sound()

        time.sleep(1)  # Delay for 1 second before taking the next moisture reading

except KeyboardInterrupt:
    GPIO.cleanup()


#In this code, we use the RPi.GPIO library to interface with the Raspberry Pi's GPIO pins. We set the GPIO mode to BCM and configure the moisture sensor pin (GPIO 17) as an input pin.

We initialize the Pygame mixer to play the sound file. Make sure you have installed the Pygame library (pip install pygame) and replace 'sound.wav' with the actual file path of the sound you want to play.

The play_sound() function loads the sound file, plays it, waits for the specified duration, and then stops the playback.
    
Inside the main loop, we continuously read the moisture level from the GPIO pin. If the moisture level drops below the threshold, we call the play_sound() function to play the sound.

The program runs until it is interrupted by a keyboard interrupt (Ctrl+C), at which point we clean up the GPIO settings.

Remember to adjust the variables (moisture_sensor_pin, moisture_threshold, sound_file, and sound_duration) according to your specific hardware setup and requirements.

Note: This example assumes you have connected the moisture sensor's signal pin to GPIO 17. Adjust the moisture_sensor_pin variable accordingly if you use a different GPIO pin. Additionally, ensure that the sound file you provide is compatible with the Pygame mixer library for playback.