import re
import sys
import command
import random

class VariableExpander:
    """Take any variables in a response and fill them with objects
    from the respective tables. Called upon locating a response"""

    def __init__(self, responseBeforeExpansion, message):
        self.resp = responseBeforeExpansion
        self.msg = message

    def expandVariables(self):
        while "$someone" in self.resp:
            while True:
                person = random.choice(self.msg.Chat.ActiveMembers)
                if person.FullName != "" and person.FullName != "Bucket":
                    break
            person = person.FullName.split(" ")[0]
            self.resp = re.sub(r"\$someone", person, self.resp, 1)
	if "$who" in self.resp:
	    self.resp = re.sub(r"\$who", self.msg.FromDisplayName, self.resp)
        while "$nouns" in self.resp:
            command.Command.databaseCursor.execute("SELECT noun FROM pluralNouns ORDER BY RANDOM() LIMIT 1")
            noun = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$nouns", noun, self.resp, 1) 
        while "$noun" in self.resp:
            sys.stdout.write(self.resp+"\r\n")
            command.Command.databaseCursor.execute("SELECT noun FROM nouns ORDER BY RANDOM() LIMIT 1")
            noun = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            sys.stdout.write(noun+"\r\n")
            self.resp = re.sub(r"\$noun", noun, self.resp, 1) 
        while "$verbs" in self.resp:
            command.Command.databaseCursor.execute("SELECT verb FROM presentVerbs ORDER BY RANDOM() LIMIT 1")
            verb = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$verbs", verb, self.resp, 1) 
        while "$verbing" in self.resp:
            command.Command.databaseCursor.execute("SELECT verb FROM ingVerbs ORDER BY RANDOM() LIMIT 1")
            verb = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$verbing", verb, self.resp, 1) 
        while "$verbed" in self.resp:
            command.Command.databaseCursor.execute("SELECT verb FROM pastVerbs ORDER BY RANDOM() LIMIT 1")
            verb = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$verbed", verb, self.resp, 1) 
        while "$verb" in self.resp:
            command.Command.databaseCursor.execute("SELECT verb FROM verbs ORDER BY RANDOM() LIMIT 1")
            verb = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$verb", verb, self.resp, 1) 
        while "$adjective" in self.resp:
            command.Command.databaseCursor.execute("SELECT adjective FROM adjectives ORDER BY RANDOM() LIMIT 1")
            verb = command.Command.databaseCursor.fetchone()[0].encode('ascii', 'ignore')
            self.resp = re.sub(r"\$adjective", verb, self.resp, 1) 
        return self.resp
