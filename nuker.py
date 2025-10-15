# Discord-Webhook-Nuker
This is a nuker (use this on your own server!)

import requests
import time

# Replace this with your Discord webhook URL
webhook_url = "YOUR_WEBHOOK_URL_HERE"

# Optional image URL (e.g. "https://example.com/image.png")
image_url = "YOUR_IMAGE_URL_HERE"

def send_message(content):
    # Create the base payload
    data = {"content": content}

    # If an image URL is provided, add it as an embed
    
   if image_url and image_url != "YOUR_IMAGE_URL_HERE":
        data["embeds"] = [{"image": {"url": image_url}}]

   response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

 # Example: Send a message every second!if set lower = ratelimiter
while True:
    send_message("YOUR_MESSAGE")
    time.sleep(1)  # wait 1 second between messages
