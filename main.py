import requests
import time

ACCESS_TOKEN = os.environ['GROUPME_TOKEN']
group_id = os.environ['GROUPME_GROUP_ID']
bot_name = "Foo-Bot"
bot_id = os.environ['GROUPME_BOT_ID']
keyword = "@foo-bar" #keyword to summon the bot

def main():
    apathy = requestApathy() #of the form (user_id, apathy level)
    if len(apathy) == 0:
        while len(apathy) == 0:
            sendMessage("Whoops, looks like there isn't enough information for me to really do much... why don't you try again?")
            apathy = requestApathy()
    cuisine = requestCuisine()
    if len(cuisine) == 0:
        while len(cuisine) == 0:
            sendMessage("Whoops, looks like there isn't enough information for me to really do much... why don't you try again?")
            cuisine = requestCuisine()
    cuisine = cuisineDict(cuisine)
    price = requestPrice()
    if price == 0:
        while price == 0:
            sendMessage("Whoops, looks like there isn't enough information for me to really do much... why don't you try again?")
            price = requestPrice()
    zips = requestZips()
    if len(zips) == 0:
         while zips == 0:
            sendMessage("Whoops, looks like there isn't enough information for me to really do much... why don't you try again?")
            zips = requestZips()

def getMessages():
    '''
    returns messages in the form [(user_id, message),...] since last bot posting.
    '''
    messages = []
    r = requests.get("https://api.groupme.com/v3/groups/{}/messages?token={}".format(group_id, ACCESS_TOKEN))
    for message in r.json()["response"]["messages"]:
        # print r.json()
        if message['name'] == bot_name:
            break;
        print message['text']
        messages += [(message['sender_id'], message['text'])]
    return messages

def hasCallWord(messages):
    return keyword.upper() in map(lambda x:x[1].upper(),messages)

def hasDone(messages):
    return "DONE" in map(lambda x:x[1].upper(),messages)

def sendMessage(message):
    r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": bot_id, "text": message})
    print "\"" + message + "\" posted\n"
def sendPictureMessage(message, image_url):
    r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": bot_id, "text": message, "picture_url": image_url})
    print "\"" + message + "\" posted with picture\n"
def requestApathy():
    '''
    returns array with [(user_id, apathy level),...] as struct
    '''
    sendMessage("(1/4) how picky are you? Reply with a number (1-10, 1 being indifferent and 10 being extremely picky) and type \"done\" when everyone is finished!")
    found = False
    while not found:
        messages = getMessages()
        if hasDone(messages):
            found = True
        time.sleep(5) 
    messages = filterForInt(messages)
    return messages

def filterForInt(messages):
    '''
    [(user_id, message)] -> [(user_id, int(message))]
    removes any invalid messages 
    '''
    for message in messages:
        try:
            message[1] = int(message[1])
        except ValueError, e:
            print "One user has entered an invalid entry:", e, message[1]
            messages.remove(message)
    return messages

def requestCuisine():
    '''
    -> [(0,0)]
    returns array with [(user_id, food_type),...] as struct
    foods list from TripAdvisor API
    '''
    foods = ['African', 'American', 'Asian', 'Bakery', 'Barbecue', 'British', 'Cafe', 'Cajun & Creole', 'Caribbean', 'Chinese', 'Continental', 'Delicatessen', 'Dessert', 'Eastern European', 'Fusion / Eclectic', 'European', 'French', 'German', 'Global / International', 'Greek', 'Indian', 'Irish', 'Italian', 'Japanese', 'Mediterranean', 'Mexican / Southwestern', 'Middle Eastern', 'Pizza', 'Pub', 'Seafood', 'Soups', 'South American', 'Spanish', 'Steakhouse', 'Sushi', 'Thai', 'Vietnamese']
    sendMessage("(2/4) what are you in the mood for? Type your favorite style of food and type \"done\" when everyone is finished!")
    found = False
    while not found:
        messages = getMessages()
        if hasDone(messages):
            found = True
        time.sleep(5)
    for message in messages:
        for food in foods:
            if message.upper() in food.upper(): #enables user to type Deli instead of delicatessen
                message[1] = food
            elif "BURGER" in message.upper(): #Handling limited edge case
                message[1] = 'American'
    return messages[:-1]

def cuisineDict(apathy, food):
    '''
    [(user_id, apathy),...], [(user_id, food),...] -> dict(food:weighted_count)
    '''
    cuisine = {}
    for (akey, avalue) in apathy:
        for (fkey, fvalue) in food:
            if akey == fkey:
                cuisine[fvalue] += int(avalue)
    return cuisine

def requestPrice():
    '''
    -> int
    returns average price 
    '''
    sendMessage("(3/4) how much are you looking to spend? On a scale of 1-4, type your price level (1 being cheapest and 4 being most expensive) and type \"done\" when everyone is finished!")
    found = False
    total = 0 #total of prices for averaging
    seen = [] #to prevent duplicate prices being posted, only last entry counts
    while not found:
        messages = getMessages()
        if hasDone(messages):
            found = True
        time.sleep(5)
    for message in reversed(messages[:-1]): #flip list for reverse chronological order
        if message[0] not in seen:
            seen += message
    for message in seen:
        total += message[1] #sum all price values
    return int(total/len(seen)) #take average with round-down (inability to spend money takes priority)

def requestZips():
    '''
    -> [str]
    returns list with [zip_code,...]
    '''
    sendMessage("(4/4) Please reply with the relevant zip code(s) and type \"done\" when everyone is finished!")
    found = False
    while not found:
        messages = getMessages()
        if hasDone(messages):
            found = True
        time.sleep(5) 
    return messages[:-1]

if __name__ == '__main__':
    main()
