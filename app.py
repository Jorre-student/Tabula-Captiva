import RPi.GPIO as GPIO
import time
import pygame  # Import the pygame library for audio
import paho.mqtt.client as mqtt

# Define amplified audio file paths
audio1 = "/home/pi/Desktop/loudest_audio_spiegel.mp3"
audio2 = "/home/pi/Desktop/loudest_audio_telefoon.mp3"
audio3 = "/home/pi/Desktop/loudest_audio_tafel.mp3"
audio4 = "/home/pi/Desktop/loudest_audio_radio.mp3"
audio5 = "/home/pi/Desktop/loudest_audio_bed1.mp3"
audio6 = "/home/pi/Desktop/loudest_audio_nacht.mp3"
audio7 = "/home/pi/Desktop/loudest_audio_wc.mp3"



MQTT_BASE_TOPIC = "zigbee2mqtt"
broker_adress = "10.150.165.14"
broker_port = 1883

def publish_mqtt_command(client, topic_suffix, payload):
    """Publishes an MQTT command to the specified topic suffix."""
    topic = f"{MQTT_BASE_TOPIC}/{topic_suffix}/set"
    result = client.publish(topic, payload)
    status = result[0]
    if status == 0:
        print(f"Published to topic: {topic} with payload: {payload}")
    else:
        print(f"Failed to publish to topic {topic}: error code {status}")

def connect_mqtt():
    """Connects to the MQTT broker and returns the client object."""
    client = mqtt.Client()
    client.connect(broker_adress, broker_port)
    return client

def disconnect_mqtt(client):
    """Disconnects from the MQTT broker."""
    client.disconnect()

def turn_off_lamp(client, friendly_name):
    """Turns off a specific lamp by its friendly name."""
    topic_suffix = friendly_name
    payload = '{"state": "OFF"}'
    publish_mqtt_command(client, topic_suffix, payload)

def turn_on_lamp(client, friendly_name):
    """Turns on a specific lamp by its friendly name."""
    topic_suffix = friendly_name
    payload = '{"state": "ON"}'
    publish_mqtt_command(client, topic_suffix, payload)

# GPIO Pin Assignments
button_pins = [17, 6, 14, 23, 25, 21, 22]  # Define buttons (GPIO 17, 6, 14, 23)
audio_files = [audio1, audio2, audio3, audio4, audio5, audio6, audio7]  # List of louder audio files
lights = [1, 2, 2, 2, 3, 4, 5]

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup buttons
for btn in button_pins:
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Buttons

# Initialize pygame mixer
device = 'Built-in Audio Digital Stereo (HDMI)'
pygame.mixer.init(devicename=device)

mqtt_client = connect_mqtt()
turn_off_lamp(mqtt_client, "lamp1")
turn_off_lamp(mqtt_client, "lamp2")
turn_off_lamp(mqtt_client, "lamp3")
turn_off_lamp(mqtt_client, "lamp4")
turn_off_lamp(mqtt_client, "lamp5")
disconnect_mqtt(mqtt_client)

def play_audio(index):
    mqtt_client = connect_mqtt()
    lamp_name = f"lamp{lights[index]}"
    audio_file = audio_files[index]

    # Define duration in seconds for each audio file
    durations = [36, 61, 41, 42, 53, 47, 53]

    print(f"Button {index+1} pressed! Turning on {lamp_name} and playing audio...")
    turn_on_lamp(mqtt_client, lamp_name)

    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.set_volume(1.0)  # Max volume
    pygame.mixer.music.play()

    time.sleep(durations[index])

    print(f"Timer finished. Turning off {lamp_name}.")
    turn_off_lamp(mqtt_client, lamp_name)

    disconnect_mqtt(mqtt_client)

while True:
    for i, button in enumerate(button_pins):
        if GPIO.input(button) == GPIO.LOW:  # If button is pressed
            play_audio(i)  # Play corresponding audio and control light

    time.sleep(0.1)  # Small delay to prevent CPU overload
