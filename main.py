import pyttsx3

motor = pyttsx3.init()

voces = motor.getProperty('voices')

motor.setProperty('voices',voces[1].id)

texto = input("que quieres que diga")

#motor.say(texto)

motor.save_to_file(texto,'test.mp3')

motor.runAndWait()