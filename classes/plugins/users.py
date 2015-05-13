"""
Created: 18.07.2013
Last modified: 15.10.2014

Author: crasbe
"""

import random
from datetime import timedelta
from datetime import datetime

import classes.config

import classes.plugins.plugin as plugin

class Users(plugin.Plugin):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        plugin.Plugin.__init__(self)
        self.config = classes.config.Config("users.ini")
        
    
    def seen(self):
        self.receiver = self.receiver.lower()
        if(self.receiver == ""):
            output = "Folgende User habe ich schon gesehen: "
            for i in self.config.sections():
                output += self.config.read(i, "name")+" "
            return output
        if(not self.config.hasSection(self.receiver)):
            return "Ich habe den User "+self.receiver+" noch nicht gesehen."
        section = self.config.readSection(self.receiver)
        
        deltaTime = datetime.now() - datetime.strptime(section["time"], "%d.%m.%Y-%H:%M:%S %Z")
        seconds = int(deltaTime / timedelta(seconds=1))
        minutes = int(seconds // 60)
        seconds %= 60
        hours = int(minutes // 60)
        minutes %= 60
        days = int(hours // 24)
        hours %= 24

        output = "{} habe ich zuletzt vor {}{}{}{} in {} gesehen."
        
        daystr = (str(days)+ (" Tagen" if days != 1 else " Tag")+", ") \
                    if days != 0 else ""
        hourstr = (str(hours)+ (" Stunden" if hours != 1 else " Stunde")+", ") \
                    if hours != 0 else ""
        minstr  = (str(minutes)+ (" Minuten" if minutes != 1 else " Minute")+" und ") \
                    if minutes != 0 else ""
        secstr  = (str(seconds)+ " Sekunden" if seconds != 1 else " Sekunde")
                        
        return output.format(section["name"], daystr, hourstr, minstr, secstr, section["channel"])
    
    def lastmsg(self):
        self.receiver =self. message.replace(self.command, "").strip()
        if(self.receiver == ""):
            return "Wessen letzte Nachricht möchtest du lesen???"
        try:
            section = self.config.readSection(self.receiver.lower())
        except self.config.NoSectionError as e:
            pass
        
        return self.receiver+" hat zuletzt in "+section["channel"]+" um "+\
                section["time"].split("-")[1]+" gesagt: \""+\
                section["message"]+"\""
