
# Parent class 1
class WiFiDevice:

    def connect_wifi(self):
        print("WiFi connected successfully")


# Parent class 2
class VoiceAssistant:

    def activate_voice(self):
        print("Voice control activated")


# Child class (Multiple Inheritance)
class SmartSpeaker(WiFiDevice, VoiceAssistant):

    def __init__(self, brand):
        self.brand = brand

    def display_details(self):
        print("Smart Speaker Brand:", self.brand)


# Creating object
speaker = SmartSpeaker("Amazon Echo")

# Calling methods
speaker.display_details()
speaker.connect_wifi()
speaker.activate_voice()
