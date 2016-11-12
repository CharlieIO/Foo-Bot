import requests
import time

ACCESS_TOKEN = os.environ['GROUPME_TOKEN']
group_id = os.environ['GROUPME_GROUP_ID']
bot_name = "Foo-Bot"

def main():
    r = requests.get("https://api.groupme.com/v3/groups/{}/messages?token={}".format(group_id, ACCESS_TOKEN))
    for message in r.json()["response"]["messages"]:
        # print r.json()
        if message['name'] == bot_name:
            break;
        print message['text']

if __name__ == '__main__':
    main()
