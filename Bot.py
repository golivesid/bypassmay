import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup

# Telegram Bot Token
TOKEN = '6827764342:AAGXmg-mTTK6yp_TYzRW99S0ToevZx-iw1Q'

# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Welcome to Terabox Video Bot! Send me a Terabox link and I'll provide you with the video.")

# Function to handle messages containing terabox links
def handle_terabox_link(update, context):
    url = update.message.text

    # Extract video link from terabox page
    video_link = get_video_link_from_terabox(url)
    
    if video_link:
        update.message.reply_text("Here is the video link: {}".format(video_link))
    else:
        update.message.reply_text("Sorry, I couldn't find any video link on this page.")

# Function to extract video link from terabox page
def get_video_link_from_terabox(url):
    try:
        # Send request to terabox link
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find video link
        video_link = soup.find('video')['src']
        
        return video_link
    except Exception as e:
        print("Error:", e)
        return None

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_terabox_link))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# Developed by Rj zala
