# Parent class 1
class WiFiDevice:
    def connect_wifi(self):
        print("WiFi Connected Successfully")


# Parent class 2
class VoiceAssistant:
    def voice_control(self):
        print("Voice Control Activated")


# Child class (Multiple Inheritance)
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display_details(self):
        print("Smart Speaker is Ready")


# Creating object
s1 = SmartSpeaker()

# Calling methods
s1.connect_wifi()
s1.voice_control()
s1.display_details()
