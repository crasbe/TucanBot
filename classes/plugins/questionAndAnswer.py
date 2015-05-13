"""
Created: 18.07.2013
Last modified: 11.05.2014

Author: crasbe
"""

import random

import classes.plugins.plugin as plugin

class QuestionAndAnswer(plugin.Plugin):
    """ QuestionAndAnswer:
    This class contains Q&A-like plugins with random results.
    Variables: 
        none
    """
    
    def __init__(self):
        """ __init__:
        The constructor executes the constructor of the parent
        and updates the list of plugins.
        Variables:
            self.plugins - from classes.plugins.plugin - type: dict
        """
        plugin.Plugin.__init__(self)


    def ping(self):
        """ ping:
        This function returns 'Pong!'. Nothing fancy.
        Variables:
            none
        """
        return "Pong!"
    
    def pingpong(self):
        """ pingpong:
        This function returns 'Pongping!'. Nothing fancy.
        Variables:
            none
        """
        return "Pongping!"
        
    def dice(self):
        """ dice:
        This function does, what a dice does.
        """
        
        random.seed()
        return str(random.randint(0, 6))
    
    def decide(self):
        """ decide:
        This function returns a random answer. Three answers are
        possible. It can also decide between >=2 possibilities.
        Variables:
            none
        Classes:
            random
        """
        random.seed()
        if (" oder " in self.message):
            elemente = self.message.split("oder")
            return elemente[random.randint(0, len(elemente)-1)].\
                    strip().replace("!decide ", "").strip("?")
        elif (" or " in self.message):
            elemente = self.message.split("or")
            return elemente[random.randint(0, len(elemente)-1)].\
                    strip().replace("!decide ", "").strip("?")
        
        rand = random.randint(0, 2)
        if (rand == 0):
            return "Ja!"
        elif (rand == 1):
            return "Nein!"
        elif (rand == 2):
            return "Frag später noch mal nach."
        else:
            return "CORE FUCKUP!"

    def eightball(self):
        """ eightball:
        This function returns a random answer from a given anwerset.
        Classes:
            random
        """
        answers = [ 'Soweit ich sehe, ja.',
                    'Bestimmt.',
                    'Wurde so entschieden.',
                    'Ziemlich wahrscheinlich.',
                    'Sieht danach aus.',
                    'Alle Anzeichen weisen darauf hin.',
                    'Ohne jeden Zweifel.',
                    'Ja.',
                    'Ja - definitiv.',
                    'Darauf kannst du dich verlassen.',

                    'Keine genaue Antwort, probier es nochmals.',
                    'Frage nochmals.',
                    'Sage ich dir besser noch nicht.',
                    'Kann ich jetzt noch nicht sagen.',
                    'Konzentriere dich und frage erneut.',

                    'Würde mich nicht darauf verlassen.',
                    'Meine Antwort ist nein.',
                    'Meine Quellen sagen nein.',
                    'Sieht nicht so gut aus.',
                    'Sehr zweifelhaft.']
        random.seed()
        return answers[random.randint(0, len(answers)-1)]
    
    def wisdom(self):
        wisdoms = ['Unter den Blinden ist der Einäugige Pirat.',
                   'Unter den Blinden ist der Einäugige schlau.',
                   'Auch ein blindes Huhn findet mal ein Ei.',
                   'Die Frau ist ja nicht automatisch intelligent, nur weil sie scheiße aussieht.',
                   'Man sollte den Arsch nie höher hängen, als man scheißen kann.',
                   'Stille Wasser sind immer die ruhigsten.',
                   'Du hast ein Gesicht wie ein Lexikon. Aufschlagen, zuschlagen und immer wieder nachschlagen.']
        
        random.seed()
        return wisdoms[random.randint(0, len(wisdoms)-1)]
    
    def song(self):
        songtext = ['Cut my life into pieces this is my last resort...',
                    'All in all it\'s just an other brick in the wall...',
                    'Lift me up, lift me up, higher now ama...',
                    'If you gave me a chance, I would take it...',
                    'Wenn nicht jetzt, wann dann? Wenn nicht hier, sag mir wo und wann...',
                    'No place I rather be...',
                    'Oh Jonny, warum hast du kein Gewissen? Ja dann kannst du dich verpissen...',
                    'But in the end, it doesn\'t even matter...',
                    'Oder in Rio im Abendwind, in jedem Arm ein schönes Kind...',
                    'Lady, running down to the riptide, taken away to the dark side...',
                    'Liar, liar! Why on earth won\'t you tell the truth?',
                    'I\'ve put my trust in you, pushed as far as I can go...',
                    'Das war mit Abstand die schlimmste Woche, die ich in meinem Leben je hatte...',
                    'Du bist und bleibst für immer ein Teil von mir...',
                    'Imagine there\'s no heaven...',
                    'She works hard for the money!']
        
        random.seed()
        return songtext[random.randint(0, len(songtext)-1)]
    
    def powerseller(self):    
        return self.sharrukin()
    
    def sharru(self):
        return self.sharrukin()
        
    def sharrukin(self):
        quote = [   "Die Preise sind nicht \"Ramsch-Würdig\", denn ich habe immer gutes Geld in meine Sachen investiert, da Geld für dieses exklusive Hobby für mich keine Rolle spielt.",
                    "Ich bin gnadenlos, wenn ich etwas haben will, und zücke da ohne zu zögern auch das Porte-Monnaie, wenn ein \"Jim-Power\" 100-120€ kosten soll.",
                    "Ich stufe die Qualität der Ware im Bereich von Zwei bis Drei ein.",
                    "Meine Wunschvorstellungen trafen da teilweise auf keinerlei Verständnis, und haben daher auch bei mir ein Umdenken ausgelöst.",
                    "Ihr wollt doch in Wahrheit nur den Preis drücken :)",
                    "Ja, sieht auf den ersten Blick vielleicht unverschämt aus, aber wenn ihr in euch geht, dann werdet ihr feststellen, dass es sich bei meiner B1260, komplett in OVP, um ein absolut seltenes Sammlerstück handelt, welches in diesem Zustand wohl kaum noch anzutreffen ist.",
                    "Die Preise bleiben so wie im ersten Post anonnciert.",
                    "wie gesagt - alles an oberflächigen Partikeln entfernt - \nBleche strahlen wie neu.\ntoller deal mit \"root\".\nIch gebe die Note Zwei (2).\nObwohl Fingerabdrücke, schwarze Pünktchen...",
                    "Ja, ich kann nicht nur techno, sondern auch melodischen rock der 80er :)",
                    "ich werde mal Dein Karma erhöhen (3 -> 4), für Deine tollen Zeitdokumente",
                    "Ach Dennis: Du hast vielleicht von vorne bis hinten recht mit deiner Argumentation.",
                    "Schön, dass wir alle konsens darüber haben, dass wir erst mal das erscheinungsdatum abwarten sollten." ]
                    
        random.seed()
        #return quote[random.randint(0, len(quote)-1)]
        return ""
    
    def gelecktvonwolfdietrich(self):
        return "Auch an mir hat Wolf Dietrich mal geleckt! *schlabber*"
     
    def quote(self):
        a500 = ['A PAGE FOR SHARON AND VONNIE TO USE',
                'PROCESSOR AND OTHER USEFUL COMPONENTS',
                'MEMORY AND...WELL, I USED TO REMEMBER',
                'PAULA DOES THINGS THAT DENISE DOESN\'T',
                'DENISE IS PRETTY MUCH INTO VIDEO...',
                'RS232, PARALLEL PORT AND KEYBOARD',
                'FLOPPY DISK AND EXPANSION CONNECTORS',
                'POWER DISTRIBUTION AND DECOUPLING']
        
        a501 = ['512K/2M-BYTE RAM EXPANSION AND CLOCK']
        
        a600 = ['DIRECTORIES AND REVISION HISTORY',
                'PROCESSOR AND OTHER USEFUL COMPONENTS',
                'MEMORY AND...WELL, I USED TO REMEMBER',
                'PAULA PREFERS THE TRADITIONAL MODES',
                'PARTY OUT OF BOUNDS, WHAT A MESS...',
                'SERIAL AND PARALLEL PORTS',
                'THE REST OF THE FLOPPY STUFF',
                'THE NEW HOME OF THE KEYBOARD VIRUS',
                'ROM - PLAIN AND FANCY - DODADS TOO!',
                'THE KISSY FACE CREDIT CARD MONSTER',
                'MEMORY EXPANSION AND THE IDE DRIVE',
                'POWER DISTRIBUTION AND DECOUPLING',
                'SHINE ON, SHINE ON',
                'US VERSION (-01) SHOWN'] # a1200 is the same, but the last page missing out

        
        a2000 = ['Something in the way she moves...',
                 'I\'m pickin\' up good vibrations...',
                 'He never could adjust to land, although he tried so hard.',
                 'Baby, we were born to run...',
                 'Memories (all alone in the moonlight)',
                 'Goes like thunder; its a Bus-Age wonder!',
                 'I wait in this place, where the sun never shines',
                 'You\'re jamming me. Quit jamming me!',
                 'Deep down inside, I\'ve got a Rock-n-Roll heart',
                 'This ain\'t no party, this ain\'t no disco this ain\'t no foolin\' around',
                 'Welcome, my son. Welcome to the Machine.',
                 'You can keep my things, they\'ve come to take me home']
        
        
        
        random.seed()
        
        if(len(self.message.split(" ")) <= 1):
            return "Not enough arguments! Expected: !quote $machine"
        elif(len(self.message.split(" ")) > 2):
            return "Too many arguments! Expected: !quote $machine"
        
        machine = self.message.split(" ")[1]
        
        if(machine == "a500"):
            return a500[random.randint(0, len(a500)-1)]
        elif(machine == "a501"):
            return a501[random.randint(0, len(a501)-1)]
        elif(machine == "a600"):
            return a600[random.randint(0, len(a600)-1)]
        elif(machine == "a1200"):
            return a600[random.randint(0, len(a600)-2)]
        elif(machine == "a2000"):
            return a2000[random.randint(0, len(a2000)-1)]
