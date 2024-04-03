import pyttsx3 #for voice processing
import datetime #To fetch date and time from the computer
import speech_recognition as sr
import openai
import webbrowser
from pygame import mixer
import os
import requests
import wikipedia
import time
from pytube import YouTube
import ctypes
import pyautogui
import winsound
import subprocess #to work on other work simoultaneously
from colorama import init, Fore, Back, Style
import psutil
import Greetings
import random
import json
import platform
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
from moviepy.editor import VideoFileClip

apikey = "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"
openai.api_key = apikey
mixer.init()

# Colors_Printing variables
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
reset = Style.RESET_ALL

#root variables
Designation = "sir"
Name = "Jarvis"
version = "1.5.0"
speed_of_speaking = 170
volume = 0.5
male_female_voice = 0 #0 for David voice and #1 for Mark voice #2 for Zira 

Jarvis = pyttsx3.init('sapi5')
voices = Jarvis.getProperty('voices')
# print(voices)
Jarvis.setProperty('voice', voices[male_female_voice].id)
Jarvis.setProperty('rate', speed_of_speaking)
Jarvis.setProperty('volume', volume)

def speak(audio):
    Jarvis.say(audio)
    Jarvis.runAndWait()
    
def play_random_video(directory):
    video_files = [f for f in os.listdir(directory) if f.endswith('.mp4') or f.endswith('.avi') or f.endswith('.mkv')]
    if not video_files:
        print("No video files found in the directory.")
        return

    video_file = os.path.join(directory, random.choice(video_files))
    print("Playing:", video_file)

    clip = VideoFileClip(video_file)
    clip.preview() 

def search_file(filename, directory):
    # Iterate through all directories and files recursively
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the filename matches
            if filename.lower() in file.lower():
                # Print the full path of the file
                print(os.path.join(root, file))
                return

def help():
    # ANSI escape codes for colors
    COLOR_RED = '\033[91m'
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_END = '\033[0m'

    # File path to the JSON data
    file_path = "Help.json"

    # Read JSON data from file
    with open(file_path, 'r') as file:
        data = file.read()

    # Parse JSON
    parsed_data = json.loads(data)

    # Print JSON with colored headings
    def print_colored(json_data, indent=0):
        for key, value in json_data.items():
            if isinstance(value, dict):
                print(COLOR_YELLOW + "  " * indent + str(key) + ":" + COLOR_END)
                print_colored(value, indent + 1)
            elif isinstance(value, list):
                print(COLOR_GREEN + "  " * indent + str(key) + ":" + COLOR_END)
                for item in value:
                    print(COLOR_GREEN + "  " * (indent + 1) + "- " + COLOR_END + str(item))
            else:
                print(COLOR_RED + "  " * (indent + 1) + str(key) + ": " + COLOR_END + str(value))

    print_colored(parsed_data)

def generate_strong_password(length=12):
    pass
    # # Define character sets for each type of character
    # uppercase_letters = string.ascii_uppercase
    # lowercase_letters = string.ascii_lowercase
    # digits = string.digits
    # special_characters = string.punctuation

    # # Ensure at least one character from each set
    # password = [
    #     random.choice(uppercase_letters),
    #     random.choice(lowercase_letters),
    #     random.choice(digits),
    #     random.choice(special_characters)
    # ]

    # # Generate remaining characters randomly
    # password.extend(random.choice(uppercase_letters + lowercase_letters + digits + special_characters) for _ in range(length - 4))
    # # Shuffle the characters to ensure randomness
    # random.shuffle(password)
    # # Convert the list of characters to a string
    # strong_password = ''.join(password)
    # return strong_password


def get_battery_percentage():
    try:
        # Get battery information
        battery = psutil.sensors_battery()

        # Check if battery information is available
        if battery is not None:
            # Calculate and print the battery percentage
            percentage = battery.percent
            print(f"Battery Percentage: {percentage}%")
            speak(f"Battery condition is {percentage} percent, it is good sir")
        else:
            print("Battery information not available on this system.")
            speak("Battery information is not available on this system, sorry for your inconvenience")

    except Exception as e:
        print(f"Error: {e}")
        
def login_to_instagram(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    try:
        # Wait for the username and password input fields to be visible
        username_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Submit the login form
        password_field.send_keys(Keys.RETURN)
        # Wait for the login process to complete
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://www.instagram.com/")
        )
    finally:
        while True:
            driver.maximize_window()
        
def fetch_phone_number_details(phone_number_str):
    try:
        phone_number = phonenumbers.parse(phone_number_str)
        # Check if the number is valid
        is_valid = phonenumbers.is_valid_number(phone_number)
        # Get number type based on the carrier type
        number_type = "Mobile" if carrier._is_mobile(number_type:=carrier.number_type(phone_number)) else "Landline"    
        # Get country name
        country = geocoder.description_for_number(phone_number, "en")
        # Get carrier information
        provider = carrier.name_for_number(phone_number, "en")
        # Get timezone information
        time_zone = timezone.time_zones_for_number(phone_number) 
        # Get formatted phone number
        formatted_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)  
        return {
            f"{yellow}Phone Number{reset}": phone_number_str,
            f"{yellow}Valid{reset}": is_valid,
            f"{yellow}Type{reset}": number_type,
            f"{yellow}Country{reset}": country,
            f"{yellow}Carrier{reset}": provider,
            f"{yellow}Timezone{reset}": str(time_zone[0]) if time_zone else None,
            f"{yellow}Formatted Number{reset}": formatted_number
        }
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return {"error": str(e)}

def play_poweroff_sound():
    try:
        subprocess.run(["powershell", "(New-Object Media.SoundPlayer 'C:\\Windows\\Media\\Windows Shutdown.wav').PlaySync()"])
    except Exception as e:
        print(f"Error playing power-off sound: {e}")

def shut_down():
    print(f"{red}shutting down the pc")
    speak(f"ok {green}{Designation}{reset} shutting down the pc")
    print("Ending all the running programs")
    speak("Ending all the running programs")
    print("aborting all the processors")
    speak("aborting all the processors")
    print("Success✔")
    speak("successfully aborted")
    speak(f"bye {Designation}{reset}")

def beep(frequency, duration):
    winsound.Beep(frequency, duration)

def shut_down_pc():
    os.system("shutdown /s /t 1")

def lock_screen():
    ctypes.windll.user32.LockWorkStation()
def unlock_screen(password):
    # Simulate pressing the Windows key to show the login screen
    pyautogui.hotkey('win')
    # Wait for a short time to ensure the login screen is visible
    time.sleep(1)
    # Type the password to unlock the screen
    pyautogui.write(password)

def youtube_download_audio(youtube_url, output_path="C:/Users/Infort/Downloads"):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)
        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Download the audio stream
        print(f"{blue}Downloading audio from {yt.title}...")
        speak(f"Downloading audio from youtube...")
        audio_stream.download(output_path)
        print(f"{green}Download complete!")
        speak(f"Download complete {Designation}")

    except Exception as e:
        print(f"Error: {e}")

def get_wifi_system_log():
    try:
        # Run the netsh command to get the system log of Wi-Fi
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True, check=True)
        # Print the system log of Wi-Fi with a gap of 0.2 seconds between each line
        print("Wi-Fi System Log:")
        lines = result.stdout.split('\n')
        for line in lines:
            print(line)
            time.sleep(0.2)
    except subprocess.CalledProcessError as e:
        print("Error:", e)        

def print_google_results():
    print("Not Available")
    speak("Not Available")
        
def news():
    # speak(f"Enter a topic {Designation}")
    random = "random"
    api_key = "pub_33117cdfdfaff7df9f4d6c4e329839abc2668"
    # search = input("Enter topic for news : ")
    response = requests.get(f"https://newsdata.io/api/1/news?apikey=pub_33117cdfdfaff7df9f4d6c4e329839abc2668&q=delhi&country=in&language=en&category=crime,entertainment,technology")
    title = response.json()['results'][0]['title']
    description = response.json()['results'][0]['description']
    content = response.json()['results'][0]['content']
    publish = response.json()['results'][0]['pubDate']

    print(f"{green}Title{reset} : \n{title}")
    speak(f"Title of the news is, \n{title}")
    print(f"\n{green}sub headlines :{reset} \n{description}")
    print(f"\n{green}Published At :{reset} \n{publish}\n")
    speak(f"\nPublished At \n{publish}\n")

def whether():
    try:
        api_key = "1ac5fe9217d14f20bca64622231311"
        print(f"Tell me the city {Designation}")
        speak(f"Tell me the city {Designation}")
        city = input(f"{green}Enter City : {reset}")
        country = "india"

        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
        forecast = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&aqi=no")
        forecast_response = forecast.json()
        whether = response.json()['current']['condition']['text']
        wind = response.json()['current']['wind_kph']
        region = response.json()['location']['region']
        localtime = response.json()['location']['localtime']
        min_temp_f = forecast_response['forecast']['forecastday'][0]['day']['mintemp_f']
        max_temp_f = forecast_response['forecast']['forecastday'][0]['day']['maxtemp_f']
        min_celsius = (min_temp_f-32/9 * 5)
        max_celsius = (max_temp_f-32/9 * 5)
        min_temp_c = min_celsius
        max_temp_c = max_celsius
        rain = forecast_response['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        snow = forecast_response['forecast']['forecastday'][0]['day']['daily_chance_of_snow']
        # astro
        sunrise = forecast_response['forecast']['forecastday'][0]['astro']['sunrise']
        sunset = forecast_response['forecast']['forecastday'][0]['astro']['sunset']
        moonrise = forecast_response['forecast']['forecastday'][0]['astro']['moonrise']
        moonset = forecast_response['forecast']['forecastday'][0]['astro']['moonset']
        mixer.music.load('C:/Users/Infort/OneDrive/Desktop/C programming Projects/Jarvis/Audios/whether.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()
        print(f"{green}Current speed of wind in {city} :{reset} {wind}kph")
        speak(f"Current speed of the wind in {city}, {country} is {wind}kilometer per hour")
        print(f"{green}Region :{reset} {region}")
        speak(f"Region , {region}")
        print(f"{green}Local_time :{reset} {localtime}")
        speak(f"local time , {localtime}")
        # forecasting
        print(f"{green}Minimum Temperature :{reset} {min_temp_f}")
        speak(f"Minimum Temperature in farenheight {min_temp_f}")
        print(f"{green}Maximum Temperature :{reset} {max_temp_f}")
        speak(f"Maximum Temperature in farenheight {max_temp_f}")
        print(f"{green}Minimum Temperature (celsius) :{reset} {min_temp_c}")
        speak(f"Minimum Temperature in celsius {min_temp_c}")
        print(f"{green}Maximum Temperature (celsius) :{reset} {max_temp_c}")
        speak(f"Maximum Temperature in celsius {max_temp_c}")
        print(f"{green}Chances of rain :{reset} {rain}%")
        speak(f"Chances of rain is {rain} percent")
        print(f"{green}Chances of snow :{reset} {snow}%")
        speak(f"Chances of snow : {snow} percent")
        print(f"{green}Sunrise Time :{reset} {sunrise}")
        speak(f"Sunrise is at {sunrise}")
        print(f"{green}Sunset Time :{reset} {sunset}")
        speak(f"Sunset is at {sunset}")
        print(f"{green}moonrise Time :{reset} {moonrise}")
        speak(f"moonrise Time is at {moonrise}")
        print(f"{green}moonset Time :{reset} {moonset}")
        speak(f"moonset Time is at {moonset}")
        print(f"{green}whether ({city}) :{reset} {whether}")
        speak(f"whether of the {city} is currently {whether}")

        mixer.music.set_endevent()
        mixer.music.stop()
    except:
        print(f"We are not able to fetch the details ! Sorry {Designation}")
        speak(f"We are not able to fetch the details ! Sorry {Designation}")

def get_system_details():
    system_details = {}
    
    # Operating System Details
    system_details["System"] = platform.system()
    system_details["Node Name"] = platform.node()
    system_details["Release"] = platform.release()
    system_details["Version"] = platform.version()
    system_details["Machine"] = platform.machine()
    system_details["Processor"] = platform.processor()
    
    # Windows Specific Details
    if system_details["System"] == "Windows":
        system_details["Windows Version"] = platform.win32_ver()[0]
    
    return system_details

def print_system_details(system_details):
    time.sleep(0.2)
    print(f"{green}System Details:{reset}")
    time.sleep(0.2)
    for key, value in system_details.items():
        print(f"{key}: {value}")
        time.sleep(0.2)

def open_brave_private_window():
    # Full path to the Brave browser executable
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    # Command to open Brave browser in private mode
    command = f'"{brave_path}" --incognito'
    try:
        # Execute the command
        subprocess.Popen(command, shell=True)
        print("Brave browser opened in private mode.")
    except Exception as e:
        print("Error:", e)

def initializing():
    print(f"{cyan}Initializing..{reset}")
    speak("Initializing..")
    print(f"{green}Initialization : success✔{reset}")
    speak("   ")
    print("Starting systems applications")
    speak("Starting systems applications")
    print(f"{green}System application init() : success✔{reset}")
    speak("   ")
    print("checking all drivers")
    speak("checking all drivers")
    print(f"{green}Drivers : Set✔{reset}")
    speak("   ")
    print("Caliberating all the core processors")
    speak("Caliberating all the core processors")
    print(f"{green}Core processors : Caliberated✔{reset}")
    speak("   ")
    print("Checking the internet connection")
    speak("Checking the internet connection")
    print(f"{green}Network connection : Connected✔{reset}")
    speak("   ")
    print("Wait a moment..")
    speak("Wait a moment..")
    print(f"{green}drivers are up and running✔{reset}")
    speak("drivers are up and running")
    print(f"{green}systems have been activated✔{reset}")
    speak("systems have been activated")
    print(f"I am online {green}{Designation} ✔{reset}")
    speak(f"I am online {Designation}")
    
def calculator():
    symbol = input("Enter the operation (+, -, *, /): ")
    if symbol not in ('+', '-', '*', '/'):
        print("Error: Invalid operation")
        return None

    values = []
    while True:
        value_str = input("Enter a value (or 'done' to finish): ")
        if value_str.lower() == 'done':
            break
        try:
            value = float(value_str)
            values.append(value)
        except ValueError:
            print("Error: Invalid value")

    if not values:
        print("Error: No values provided")
        return None

    result = values[0]
    for value in values[1:]:
        if symbol == '+':
            result += value
        elif symbol == '-':
            result -= value
        elif symbol == '*':
            result *= value
        elif symbol == '/':
            if value == 0:
                print("Error: Division by zero!")
                return None
            result /= value

    return result

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms?\nBecause they make up everything!",
        "What do you call a fish with no eyes?\nFsh!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What did one plate say to the other plate?\nDinner's on me!",
        "Why don't skeletons fight each other?\nThey don't have the guts!",
        "Did you hear about the mathematician who's afraid of negative numbers?\nHe'll stop at nothing to avoid them!",
        "Why don't seagulls fly over the bay?\nBecause then they'd be called bagels!",
        "Why did the bicycle fall over?\nBecause it was two-tired!",
        "What did one hat say to the other?\nYou stay here, I'll go on ahead!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "I'm reading a book on the history of glue.\nI just can't seem to put it down!",
        "What do you call fake spaghetti?\nAn impasta!",
        "Why did the coffee file a police report?\nIt got mugged!",
        "I used to play piano by ear.\nNow I use my hands!",
        "Why did the golfer bring two pairs of pants?\nIn case he got a hole in one!",
        "What did the big flower say to the little flower?\nWhat's up, bud?",
        "Why did the hipster burn his tongue?\nHe drank his coffee before it was cool!",
        "I'm on a whiskey diet.\nI've lost three days already!",
        "Why don't skeletons fight each other?\nThey don't have the guts!",
        "Why did the computer go to the doctor?\nBecause it had a virus!",
        "I'm reading a book on anti-gravity.\nIt's impossible to put down!",
        "Why don't eggs tell jokes?\nBecause they'd crack each other up!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "What's orange and sounds like a parrot?\nA carrot!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire?\nFrostbite!",
        "What's a vampire's favorite fruit?\nA blood orange!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire?\nFrostbite!",
        "What's a vampire's favorite fruit?\nA blood orange!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire?\nFrostbite!",
        "What's a vampire's favorite fruit?\nA blood orange!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire?\nFrostbite!",
        "What's a vampire's favorite fruit?\nA blood orange!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!",
        "I told my wife she was drawing her eyebrows too high.\nShe looked surprised!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire?\nFrostbite!",
        "What's a vampire's favorite fruit?\nA blood orange!"
    ]

    return random.choice(jokes)


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(f"{green}Good Morning :){reset}")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print(f"{green}Good Afternoon :){reset}")
        speak("Good Afternoon")
    
    else:
        print(f"{green}Good Evening{reset}")
        speak("Good Evening")
        
    mixer.music.load('C:/Users/Infort/OneDrive/Desktop/Confidentials/Jarvis/Audios/bg.mp3') # Enter your background music path
    mixer.music.set_volume(0.2)
    mixer.music.play()
    print(f"Version : {version}")
    # Fetch WiFi details
    get_wifi_system_log()
    
    system_details = get_system_details()
    print_system_details(system_details)
    mixer.music.set_endevent()
    mixer.music.stop()
    time.sleep(0.2)

def ai():
    chat_log = []

    while True:
        user_message = input("Enter Chat : ")
        if user_message.lower() == "quit":
            break
        else:
            chat_log.append({"role" : "user", "content": user_message})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo-16k-0613",
                messages = chat_log,
                temperature=1,
                max_tokens=64,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            assistant_response = response['choices'][0]['message']['content']
            print("AI : ", assistant_response, "\n")
            AI = assistant_response
            speak(AI)
            chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
    
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print(f"{yellow}Listening...{reset}")
            r.pause_threshold = 1
            audio = r.listen(source)
    except:
        print("No Microphone available")

    try:
        print(f"{blue}Recognizing...{reset}")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"{red}-->{reset} {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print(f"Say that again please... {red}:){reset}")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def main():
    # Generated_password = generate_strong_password(12)
    # data = {
    #     "Version": version,
    #     "System Details": "Can not be shown here",
    #     "Wifi Details": "Can not be shown here",
    #     "password": Generated_password
    # }   
    # with open('password.json', 'w') as file:
    #     json.dump(data, file, indent=4)
    # wakeup_password = input("Enter Pin : ")
    # if (wakeup_password==Generated_password):
        wish()
        while True:
            # query = takeCommand().lower()
            query = input(f"{yellow}--> {reset}").lower()

            if "chat" in query:
                print(f"What can i search {Designation}")
                speak(f"What can i search {Designation}")
                ai()
        
            elif "hello" in query:
                random_greetings = random.choice(Greetings.greetings)
                print(random_greetings)
                speak(random_greetings)

            elif "search" in query:
                query = query.replace("search", "")
                print(f"Searching {Designation}..")
                speak(f"Searching {Designation}..")
                webbrowser.open_new_tab(query)
                print(f"{green}Searched {reset}{query}")
                speak(f"Searched {query}")
            
            elif query == "open youtube":
                webbrowser.open("youtube.com")
                print(f"{green}Opening youtube :){reset}")
                speak("Opening youtube")

            elif "find youtube" in query:
                print(f"What can i search {Designation}")
                speak(f"What can i search {Designation}")
                search = input("Enter Search : ")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                print("Opening youtube :)")
                speak("Opening your search in youtube")
            
            elif "open google" in query:
                webbrowser.open("google.com")
                print(f"{green}Opening google :){reset}")
                speak("Opening google")
        
            elif "open browser" in query:
                print(f"{green}opening webbrowser{reset}")
                speak("opening webbrowser")
                browser = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
                os.startfile(browser)

            elif "open vscode" in query:
                print(f"{reset}opening vscode{green}")
                speak("opening vscode")
                vscode = "C:/Users/Infort/AppData/Local/Programs/Microsoft VS Code/Code.exe"
                os.startfile(vscode)
        
            elif "open gmail" in query:
                print(f"{green}opening gmail{reset}")
                speak("opening gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif "open email" in query:
                print(f"{green}opening email{reset}")
                speak("opening email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif "open files" in query:
                print(f"{green}opening file explorer{reset}")
                speak("opening file explorer")
                files = "c:/"
                os.startfile(files)
            elif "open file explorer" in query:
                print("opening file explorer")
                speak("opening file explorer")
                files = "c:/"
                os.startfile(files)
        
            elif "open ppsspp" in query:
                print("opening playstation emulator")
                speak("opening playstation emulator")
                ppsspp = "C:/Program Files/PPSSPP/PPSSPPWindows64.exe"
                os.startfile(ppsspp)

            elif "open sublime" in query:
                print("opening sublime text editor")
                speak("opening sublime text editor")
                sublime = "C:/Program Files/Sublime Text/sublime_text.exe"
                os.startfile(sublime)

            elif "open whatsapp" in query:
                print("opening whatsapp")
                speak("opening whatsapp")
                webbrowser.open("web.whatsapp.com")

            elif "open instagram" in query:
                print("opening instagram")
                speak("opening instagram")
                webbrowser.open("instagram.com")

            elif "open facebook" in query:
                print("opening facebook")
                speak("opening facebook")
                webbrowser.open("facebook.com")
        
            elif "open chatgpt" in query:
                print("opening chatbot")
                speak("opening chatbot")
                webbrowser.open("chat.openai.com")
        
            elif "open openai overview" in query:
                print("opening playground of openai")
                speak("opening playground of openai")
                webbrowser.open("https://platform.openai.com/overview")
            elif "open openai playground" in query:
                print("opening playground of openai")
                speak("opening playground of openai")
                webbrowser.open("https://platform.openai.com/overview")


            elif "make file" in query:
                print(f"ok {Designation} but give a name to your file")
                speak(f"ok {Designation} , but give a name to your file")
                query = input("Enter your file name : ").lower()
                f = open(query, "a")
                print(f"Your file has been created {Designation}")
                speak(f"Your file ({query}.txt) has been created ")
            elif "make file in same directory" in query:
                print(f"ok {Designation} but give a name to your file")
                speak(f"ok {Designation} , but give a name to your file")
                query = input("Enter your file name : ").lower()
                f = open(query, "r+")
                print(f"Your file has been created {Designation}")
            elif "file in specific directory" in query:
                print(f"ok {Designation}, but give a name to your file")
                speak(f"ok {Designation}, but give a name to your file")
                query = input("Enter your file name : ").lower()
                f = open(query, "r+")
                print(f"Your file has been created {Designation}")
        
            elif "hide files" in query:
                print(f"Hiding all files {Designation}")
                speak(f"Hiding all files {Designation}")
                os.system("attrib +h /s /d")
                print("All files are hidden")
                speak("All files are hidden")

            elif "show files" in query:
                print(f"Unhiding all files {Designation}")
                speak(f"Unhiding all files {Designation}")
                os.system("attrib -h /s /d")
                print("All files are Unhidden")
                speak("All files are Unhidden")

            elif "whether" in query:
                whether()
        
            elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                try:
                    print('Searching Wikipedia...')
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    print("Fetching Summary")
                    speak("fetching summary")
                    print(f"{red}According to Wikipedia ,{reset}")
                    speak("according to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Wikipedia disambiguation error: {e}")
                except wikipedia.exceptions.HTTPTimeoutError as e:
                    print(f"Wikipedia HTTP timeout error: {e}")
                except wikipedia.exceptions.PageError as e:
                    print(f"Wikipedia page error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                
            elif "song" in query:
                import RandomSongs #file
                # Specify the folder containing the music files
                print(f"playing song {Designation}")
                speak(f"Enjoy the song")
                music_folder = "C:/Users/Infort/OneDrive/Desktop/Confidentials/Songs"
                RandomSongs.play_random_song(music_folder)
                print("Thanks for using J.A.R.V.I.S Music System")
                
            elif "find in pc" in query:
                # Example usage:
                speak("Enter File name")
                filename_to_search = input("Enter the name of the file you want to search for: ")
                speak("Specify the Directory")
                directory_to_search = input("Enter the directory to search in (leave blank for current directory): ")

                # If no directory is provided, use the current directory
                if directory_to_search == "":
                    directory_to_search = "."

                search_file(filename_to_search, directory_to_search)
                
            elif "play video" in query:
                speak("Enjoy the Video")
                directory_path = "C:/Users/Infort/OneDrive/Desktop/Confidentials/Jarvis/Videos"
                play_random_video(directory_path)
                print("Thanks for using J.A.R.V.I.S Video System")

        
            elif "google" in query:
                print_google_results()

            elif query == "battery":
                get_battery_percentage()

        
            elif "exit" in query:
                print(f"ok {Designation}")
                speak(f"ok {Designation}")
                exit()

            elif "current time" in query:
                current_datetime = datetime.datetime.now()
                # Extract hour and minute
                current_hour = current_datetime.hour
                current_minute = current_datetime.minute
                # Display the result
                print(f"Current time: {current_hour}:{current_minute}")
                speak(f"Current time is {current_hour} hours and {current_minute}minute")
        
            elif "news" in query:
                news()

            elif "download audio" in query:
                print("Enter url please")
                speak(f"Please enter the url {Designation}")
                yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> "))) 
                video = yt.streams.filter(only_audio=True).first() 
                destination = "C:/Users/Infort/Downloads"
                out_file = video.download(output_path=destination)  
                base, ext = os.path.splitext(out_file) 
                new_file = base + '.mp3'
                os.rename(out_file, new_file) 
                speak(yt.title + " has been successfully downloaded.")
                print(yt.title + " has been successfully downloaded.")
        
            elif "how are you" in query:
                print(f"I am Good {Designation}")
                speak(f"I am Good {Designation}")
            elif "who are you" in query:
                print(f"I am {Name}")
                speak(f"I am {Name}")
            elif "whats your name" in query:
                print(f"My name is {Name}, and i am a artificial intelligence")
                speak(f"My name is {Name}, and i am a artificial intelligence")
            elif "who made you" in query:
                print(f"I a an AI {Name}, AJ Made me")
                speak(f"I a an A I, my name is {Name}, and A J industries Made me")

            elif "how are you" in query:
                print(f"I am Good {Designation}")
                speak(f"I am Good {Designation}")
            elif "who are you" in query:
                print(f"I am {Name}")
                speak(f"I am {Name}")
            elif "whats your name" in query:
                print(f"My name is {Name}, and i am a artificial intelligence")
                speak(f"My name is {Name}, and i am a artificial intelligence")
            elif "who made you" in query:
                print(f"I a an AI {Name}, Bubbles Made me")
                speak(f"I a an A I {Name} Bubbles Made me")
            elif "what are you doing" in query:
                print(f"I am doing nothing {Designation}")
                speak(f"I am doing nothing {Designation}")
            elif "coffe or tea" in query:
                print(f"I prefer Coffee {Designation}")
                speak(f"I prefer Coffee {Designation}")
            elif "good" in query:
                print(f"I am also {Designation}")
                speak(f"I am also {Designation}")
            elif "nice" in query:
                print(f"I am also {Designation}")
                speak(f"I am also {Designation}")
            elif "better" in query:
                print(f"I am also {Designation}")
                speak(f"I am also {Designation}")
            
            elif "private tab" in query:
                print("Opening Brave's Private window")
                speak("Opening Brave Private window")
                open_brave_private_window()
                print(f"{green}Successfully Done.{reset}")
        
            elif "calculate" in query:
                speak("As your wish")
                print("Result:", calculator())
            
            elif "calculator" in query:
                speak("As your wish")
                print("Result:", calculator())
        
            elif "tell me a joke" in query:
                joke = tell_joke()
                print(joke)
                speak(joke)
                mixer.music.load('C:/Users/Infort/OneDrive/Desktop/Confidentials/Jarvis/Audios/laugh.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                time.sleep(1)
            
            elif "phone number" in query:
                speak("Enter the Number")
                phone_number = input("Enter phone number (with country code): ")
                details = fetch_phone_number_details(phone_number)
                if "error" in details:
                    print("Error:", details["error"])
                else:
                    print("Phone Number Details:")
                for key, value in details.items():
                    time.sleep(0.2)
                    print(f"{key}: {value}")
        
            elif "login instagram" in query:
                # Load credentials from JSON file
                with open('C:/Users/Infort/OneDrive/Desktop/Confidentials/Jarvis/credentials.json', 'r') as file:
                    credentials = json.load(file)

                # Retrieve username and password from credentials
                username = credentials.get('username')
                passwrd = credentials.get('passwrd')

                # Check if credentials were loaded successfully
                # if username and passwrd:
                try:
                    print("Username:", username)
                    print("Password:", passwrd)
                    speak("Logged in Successfully")
                    login_to_instagram(username, passwrd)
                except Exception as e:
                    print(e)
                finally:
                    continue
        
            elif "make password":
                print("Not available now")
                print("will be available in 1.6.0")
                # password_length = int(input("Enter the length of the password: "))
                # print("Generated Strong Password:", generate_strong_password(password_length))

            elif "lock screen" in query:
                print(f"locking the screen {Designation}")
                speak(f"locking the screen {Designation}")
                lock_screen()
                password = ''
                unlock_screen(password)

            elif "shut down" in query:
                shut_down()
                play_poweroff_sound()
                shut_down_pc()
                # beep(60, 1000)

            elif "help" in query:
                help()
                print("This is all i can do")
                speak("This is all i can do")
                
            else:
                print("Sorry! I can't assist you with that")

main()
#Here Ends the J.A.R.V.I.S