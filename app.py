import pyautogui
import time

# Function to type a URL and press Enter
def type_url_and_enter(url):
    try:
        # Sleep for 3 seconds before starting to allow time to switch to the target window
        time.sleep(3)

        # Number of times to repeat typing and pressing Enter
        repeat_times = 5

        for i in range(repeat_times):
            # Type the URL
            pyautogui.write(url)
            
            # Press Enter
            pyautogui.press("enter")
            
            # Optional delay between actions
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# URL to type and press Enter
url = "https://youtu.be/y8hocd8vnSs"

# Call the function to type URL and press Enter
type_url_and_enter(url)

# python3 app.py




# import pywhatkit as kit
# import datetime

# number = '+923377916802'
# message = "Hello, this is a test message!"



# # Calculate the time for sending the message
# now = datetime.datetime.now()
# delay_seconds = 10  # 10 seconds delay
# send_time = now + datetime.timedelta(seconds=delay_seconds)

# # Print the scheduled send time
# print(f"Message will be sent at: {send_time}")

# # Schedule the message
# kit.sendwhatmsg(number, message, send_time.hour, send_time.minute + 1)  # Adjusting the minute by 1 to ensure it's sent after WhatsApp opens
