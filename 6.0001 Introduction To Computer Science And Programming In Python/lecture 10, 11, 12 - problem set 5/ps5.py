# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower().translate(str.maketrans('', '', string.punctuation))
        
    def is_phrase_in(self, text):
        # process text: lowercase and replace all punctuations with ' '
        low = text.lower().translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        # Now split will only contains valid words without punctuations
        lst = low.split()
        # 1st: check if the processed text contains the phrase if both removed all ' '
        if self.phrase.translate(str.maketrans('', '', ' ')) in low.translate(str.maketrans('', '', ' ')):
            # 2nd: check if each the words in phrase appear entirely in the text
            for word in self.phrase.split():
                if word not in lst:
                    return False
            return True
        else:
            return False
        
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
        
        
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, string):
        tz = pytz.timezone('EST')
        self.datetime = datetime.strptime(string, "%d %b %Y %H:%M:%S").replace(tzinfo=tz)

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.datetime.timestamp() > story.get_pubdate().timestamp()

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.datetime.timestamp() < story.get_pubdate().timestamp()

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
        
    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)
    
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, other_trigger1, other_trigger2):
        self.other_trigger1 = other_trigger1
        self.other_trigger2 = other_trigger2
        
    def evaluate(self, story):
        return self.other_trigger1.evaluate(story) and self.other_trigger2.evaluate(story)
    
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, other_trigger1, other_trigger2):
        self.other_trigger1 = other_trigger1
        self.other_trigger2 = other_trigger2
        
    def evaluate(self, story):
        return self.other_trigger1.evaluate(story) or self.other_trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    new_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                new_stories += [story]
                break
    return new_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_list = [] # contains all triggers from file
    return_list = []  # contains all triggers that are added
    trigger_dict = {'TITLE': TitleTrigger, 'DESCRIPTION': DescriptionTrigger, 'AFTER': AfterTrigger, 'BEFORE': BeforeTrigger, 'NOT': NotTrigger, 'AND': AndTrigger, 'OR': OrTrigger}
    for line in lines:
        split = line.split(',')
        for i in range(len(split)):
            if split[i].strip('t').isnumeric(): # process strings of format: t+number 
                split[i] = int(split[i].strip('t')) - 1 # turn these strings into their int - 1 to use them as index       
        trigger_obj = trigger_dict.get(split[1], False) # trigger_obj is either an object of type Trigger, or False
        if trigger_obj:
            if split[1] in ['AND', 'OR']: # these objects needs 2 args for init
                trigger_obj.__init__(trigger_obj, trigger_list[split[-2]], trigger_list[split[-1]])
            elif split[1] == 'NOT': # same as above but only need 1 arg for init
                trigger_obj.__init__(trigger_obj, trigger_list[split[-1]])
            else: # the rest only need 1 arg for init, but the arg is of type string
                trigger_obj.__init__(trigger_obj, split[-1])
            trigger_list += [trigger_obj]
        else:
            for indx in split[1:]:
                return_list += [trigger_list[indx]]

    return return_list
    


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

