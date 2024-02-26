# Importing necessary modules
from info import *
import os

twrp_building_script = "build_twrp.sh"

# Setting up variables for group ID and group URL
request_id = -4177520948
group_url = "https://t.me/+LcVNpdqBaMlmNjg0"

# Function to handle commands received by the bot
def command(m): 
    # Check if the received command is "/start"
    if m.text == "/start":
        # Reply with a message containing the group join link
        bot.reply_to(m, f"Hi, if you want to use me please join this group: {group_url}")
        bot.send_message(m.chat.id, f"This bot is created by: {bot_creator}")
    # Check if the received command starts with "/request"
    if m.text.split()[0] =="/request":
        # Check if the user is in the correct group to make requests
        if m.chat.id == request_id:
            # Call the request function to process the request
            request_twrp_build(m)
        else:
            # Reply with a message asking the user to join the correct group
            bot.reply_to(m, f"Please join this group and use me there: {group_url}")

def request_twrp_build(m):
    try:
        # Extract the URL from the user's message
        Manifest_URL = m.text.split()[1]
        Manifest_Branch = m.text.split()[2]
        Device_Tree_URL = m.text.split()[3]
        Device_Tree_Branch = m.text.split()[4]
        Device_Path = m.text.split()[5]
        Device_Name = m.text.split()[6]
        Makefile_Name = m.text.split()[7]
        Build_Target = m.text.split()[8]
        # Execute one of the dumping scripts with the URL as an argument
        result = os.system(f'bash {twrp_building_script} {Manifest_URL} {Manifest_Branch} {Device_Tree_URL} {Device_Tree_Branch} {Device_Path} {Device_Name} {Makefile_Name} {Build_Target}')
        # Check the result of the script execution
        if result == 0:
            # Reply with a success message if the script executed successfully
            bot.reply_to(m, "Successfully requested the build!")
        else:
            # Reply with an error message if something went wrong during script execution
            bot.reply_to(m, "Something went wrong")
    except:
        # Reply with a message indicating that a URL is needed for the request
        bot.reply_to(m, "I need the device tree URL to work")
        bot.reply_to(m, "Usage is as follows: /request (Manifest_URL) (Manifest_Branch) (Device_Tree_URL) (Device_Tree_Branch) (Device_Path) (Device_Name) (Makefile_Name) (Build_Target)")
        bot.reply_to(m, "Example: /request https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp twrp-12.1 https://github.com/TeamWin/android_device_asus_I003D android-12.1 device/asus/I003D I003D twrp_I003D recovery")