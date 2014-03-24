import os
import oauth2
import json
import glob
# import tumblepy

# Login to tumblr api
REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
CONSUMER_KEY = 'nwLCRoEmWpj1nWg9WK2Es68ziEhUnDkBbql2e39m9ImK9qOxoc'
CONSUMER_SECRET = '4fwbkvHJMCBH9yXHtiww3moCJPUr2itd6QsEWrqlqi9hGh2YxU'

consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth2.Client(consumer)

# Controller for adding a new folder
def newFolder():
    with open("config.json", "a") as outfile:
        pathInput = raw_input("Path to files: ")
        frequencyInput = raw_input("Frequency in minutes: ")
        whichBlog = raw_input("Blog: ")
        tagsInput = raw_input("Common tags, comma separated: ")
        data = [{'folderPath': pathInput, 'frequency': frequencyInput, 'blog': whichBlog, 'tags': tagsInput}]
        outfile.write(json.dumps(data)+"\n")

# Controller for changing the settings 
def editFolder(selectedFolder):
    with open("config.json", "w") as outfile:
        pass
        

# Controller for deleting a folder
def deleteFolder(selectedFolder):
    pass

        
# Controller for creating the schedules
def makeSchedule():
    with open("config.json", "r") as outfile:
        configurations = outfile.readlines()
        for folder in configurations:
            # Do thing with path
            # Do thing with frequency
            # Correct blog
            # Do thing with tags

if __name__ == "__main__":
    makeSchedule()