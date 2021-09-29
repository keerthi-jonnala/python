#pip install pyttsx3
#to speech conversion
import pyttsx3
speaker=pyttsx3.init()

#to get the voice rate
rate=speaker.getProperty("rate")
print(rate)
rate=speaker.setProperty("rate",198)

#to get voice tone
voice=speaker.getProperty("voice")
print(voice)
#voice=speaker.setProperty("voice",voice[1].id)

#say method on the engine that passing input text to be spoken
speaker.say("Hello world")
speaker.say("Hi iam speaking machine. Thank you for listning to me")
speaker.say("omg python! I am loving you for this")
