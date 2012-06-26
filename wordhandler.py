import command
class wordHandler:    
    """This class depends heavily on the command class being open. Ensure that this is the
    case before using this class!"""
    
    def __init__(self, parsedcommand.Command, listOfTerms):
        """Perform the initial operations on the respective tables in the database.
        This will add or delete the provided word"""

        self.parsedcommand.Command = parsedcommand.Command

        if self.parsedcommand.Command == "verb+":
            command.Command.databaseCursor.execute('''INSERT INTO verbs VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verb-":
            command.Command.databaseCursor.execute('''DELETE FROM verbs WHERE verb = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbs+":
            command.Command.databaseCursor.execute('''INSERT INTO presentVerbs VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbs-":
            command.Command.databaseCursor.execute('''DELETE FROM presentVerbs WHERE verb = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbing+":
            command.Command.databaseCursor.execute('''INSERT INTO ingVerbs VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbing-":
            command.Command.databaseCursor.execute('''DELETE FROM ingVerbs WHERE verb = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbed+":
            command.Command.databaseCursor.execute('''INSERT INTO pastVerbs VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "verbed-":
            command.Command.databaseCursor.execute('''DELETE FROM pastVerbs WHERED verb = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "noun+":
            command.Command.databaseCursor.execute('''INSERT INTO nouns VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "noun-":
            command.Command.databaseCursor.execute('''DELETE FROM nouns WHERE noun = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "nouns+":
            command.Command.databaseCursor.execute('''INSERT INTO pluralNouns VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "nouns-":
            command.Command.databaseCursor.execute('''DELETE FROM pluralNouns WHERE noun = "{0}"
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "adjective+":
            command.Command.databaseCursor.execute('''INSERT INTO adjectives VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))
        elif self.parsedcommand.Command == "adjective+":
            command.Command.databaseCursor.execute('''INSERT INTO adjectives VALUES ("{0}")
                                           '''.format(' '.join(listOfTerms)))

    def writeChanges(self):
        """Commit the changes to the database and return the required output,
        indicating whether the operation was a success or not."""
        try:
            command.Command.database.commit()
            if "+" in self.parsedcommand.Command:
                return "Added successfully"
            else:
                return "Deleted successfully"

        except:
            return "Operation Failed!"


