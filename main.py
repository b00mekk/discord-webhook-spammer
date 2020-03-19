import requests
from discord_webhooks import DiscordWebhooks

webhook_url = input('Enter WEBHOOK URL: ')

message = input('Enter Message: ')
ilosc = int(input('Enter Amount of Messages: '))


webhook = DiscordWebhooks(webhook_url)

webhook.set_content(title='get spammed nwords',
                    description=message,
                    color=0xF58CBA)

webhook.set_footer(text='made by: b00mek#1314')



for i in range(ilosc):
    webhook.send()
