from gtts import gTTS
import os

def text_to_speech():
    print("--- Text to Speech Converter ---")
    text = input("Enter the text you want to convert to speech: ")
    
    if text.strip():
        try:
            print("Converting...")
          
            tts = gTTS(text=text, lang='en')
            
           
            filename = "output_speech.mp3"
            tts.save(filename)
            print(f"Successfully saved to {filename}")
        
            print("Playing audio...")
            os.startfile(filename)
            
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("You didn't enter any text.")

if __name__ == "__main__":
    text_to_speech()
