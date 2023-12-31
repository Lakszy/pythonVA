import pyttsx3

if __name__ == '__main__':
    while True:    
        x = input("Enter the word you want to hear loud: ")
        if x == "q":
            engine = pyttsx3.init()
            engine.say("Exited Sorry")
            engine.runAndWait()
            break
        
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()

        
    
