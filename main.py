import requests
import time

ACCESS_TOKEN = os.environ['GROUPME_TOKEN']
group_id = os.environ['GROUPME_GROUP_ID']
bot_name = "Foo-Bot"
keyword = "@foo-bar" #keyword to summon the bot

def main():
    messages = getMessages()
    print hasKeyword(messages)


def getMessages():
    messages = []
    r = requests.get("https://api.groupme.com/v3/groups/{}/messages?token={}".format(group_id, ACCESS_TOKEN))
    for message in r.json()["response"]["messages"]:
        # print r.json()
        if message['name'] == bot_name:
            break;
        print message['text']
        messages += [message['text']]
    return messages

def hasKeyword(messages):
    return keyword.upper() in map(lambda x:x.upper(),messages)

if __name__ == '__main__':
    main()
