import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties of the text-to-speech engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)

# Get input from the user
text = input("Enter the text that you want to convert to speech: ")

# Convert the input text to speech
engine.say(text)

# Save the output as an audio file
engine.save_to_file(text, 'output.mp3')

# Run the text-to-speech engine
engine.runAndWait()
