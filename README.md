# F🍔🍟Bot (FooBot)
A GroupMe bot to collaboratively discover your next food-adventure. 🍽
##Setup / Usage

1. Clone it!

2. Set your environment variables for the Trip Advisor Partner API key, GroupMe access token, ID of the group where the bot should function, and GroupMe bot ID. The files which contain references to these variables are **main.py** and **trip_advisor_api.py**.
 *Optional: customize the keyword and the bot_name.*

3. Gather requirements on server: `pip install -r requirements.txt`
4. Run the bot! In the Foo-Bot directory, run the following command (Linux assumed): `. run.sh &` and the bot will begin to run in the background.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request!

### Inspiration
Everyone's hungry, everyone wants to eat together, but no decisions are made. This is a common problem around the world, but especially in college towns across America, where GroupMe is the communication method of choice for friends. FooBot works to solve this problem. 
### What it does
FooBot quizzes each member of a group chat about their preferences, pickiness, budget and location in a conversational format. Given that information, and using a little bit of magic, it returns the most equidistant restaurant that everyone will enjoy. 
### How we built it
Python scripts hosted on Amazon EC2, maintained and monitored with bash scripts.
### Accomplishments that we're proud of
We were able to solve a common real-life problem. This can not be said by most, even at hackathons! This is not a tech demo, or a server built with Haskell, but instead a real finished product that will make our lives easier. 
### What we learned
Server-sided automatic error handling was a chore, but we eventually accomplished it.  
### What's next for FooBot
We hope to eventually expand to further chat platforms and offer suggestions for other services such as entertainment, hikes etc. In the future we could even build FooBot into a web-client where friends would not have to rely on chat services.
