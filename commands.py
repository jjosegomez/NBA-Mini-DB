import re

# data structures (array of objects)
coachesArray = list()
teamsArray = list()

class Coaches:
    def __init__(self, ID, SEASON, FIRST_NAME, LAST_NAME, SEASON_WIN, SEASON_LOSS, PLAYOFF_WIN, PLAYOFF_LOSS, TEAM):
        self.ID = ID
        self.SEASON = SEASON
        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.SEASON_WIN = SEASON_WIN
        self.SEASON_LOSS = SEASON_LOSS
        self.PLAYOFF_WIN = PLAYOFF_WIN
        self.PLAYOFF_LOSS = PLAYOFF_LOSS
        self.TEAM = TEAM

    def print_coach(self):
        print("{}\t{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(self.ID, self.SEASON, self.FIRST_NAME, self.LAST_NAME, self.SEASON_WIN, self.SEASON_LOSS, self.PLAYOFF_WIN, self.PLAYOFF_LOSS, self.TEAM))

class Teams:
    def __init__(self, ID, LOCATION, NAME, LEAGUE):
        self.ID = ID
        self.LOCATION = LOCATION
        self.NAME = NAME
        self.LEAGUE = LEAGUE
    
    def print_team(self):
        print("{}\t\t{}\t\t{}\t\t{}".format(self.ID, self.LOCATION, self.NAME, self.LEAGUE))

# This is the main function where the user will choose the commands
def main():
    print("welcome to the NBA mini database")
    cmd = ""
    while True:
        raw_cmd = input("enter command or finish by typing \"exit\": ")
        cmd = raw_cmd.split() #split the string if " "

        if cmd[0] == "exit":
            print("program terminated...")
            return

        if cmd[0] == "add_coach":
            add_coach(coachesArray,cmd)

        elif cmd[0] == "add_team":
            add_team(teamsArray,cmd)

        elif cmd[0] == "load_coaches":
            load_coaches(coachesArray,cmd)

        elif cmd[0] == "load_teams":
            load_teams(teamsArray,cmd)

        elif cmd[0] == "print_coaches":
            print_coaches(coachesArray)

        elif cmd[0] == "print_teams":
            print_teams(teamsArray)

        elif cmd[0] == "coaches_by_name":
            coaches_by_name(coachesArray,cmd)

        elif cmd[0] == "teams_by_city":
            teams_by_city(coachesArray,teamsArray,cmd)

        elif cmd[0] == "best_coach":
            best_coach(coachesArray,cmd)

        #"search_coaches first_name=John season_win=40" 
        elif cmd[0] == "search_coaches":
            search_coaches(coachesArray, cmd)

        elif cmd[0] == "help":
            print("The available commands are the following:")
            print("*\tadd_coach")
            print("*\tadd_team")
            print("*\tload_coaches")
            print("*\tload_teams")
            print("*\tprint_coaches")
            print("*\tprint_teams")
            print("*\tcoaches_by_name")
            print("*\tteams_by_city")
            print("*\tbest_coach")
            print("*\tsearch_coaches")

        else:
            print("invalid command. try again")
        
#this function takes in 9 arguments: ID, SEASON, FIRST_NAME, LAST_NAME, SEASON_WIN, SEASON_LOSS, PLAYOFF_WIN, PLAYOFF_LOSS, TEAM
#and adds them to the coach data base.
def add_coach(coachesArray,cmd):

    #consists of less than 7 capital letters and two digits
    ID = cmd[1]
    ID_PATTERN = r"^[A-Z]{1,7}[0-9]{1,2}$"
    matchID = re.search(ID_PATTERN, ID)
    while matchID == None:
        NEW_ID = str(input("try again. enter coach id (7 capital letters and 2 integers): "))
        matchID = re.search(ID_PATTERN, NEW_ID)
    
    #4 digits
    SEASON = cmd[2]
    SEASON_PATTERN = r"[0-9]{4}"
    matchSEASON = re.search(SEASON_PATTERN, SEASON)

    while matchSEASON == None:
        NEW_SEASON = str(input("try again. enter coach id (4 digit number): "))
        matchSEASON = re.search(SEASON_PATTERN, NEW_SEASON)

    #english name
    FIRST_NAME = cmd[3]
    FIRST_NAME_PATTERN = r"^[a-zA-Z]{2,}$"
    matchFIRST_NAME = re.search(FIRST_NAME_PATTERN, FIRST_NAME)

    while matchFIRST_NAME == None:
        NEW_FIRST_NAME = str(input("try again. enter first name: "))
        matchFIRST_NAME = re.search(FIRST_NAME_PATTERN, NEW_FIRST_NAME)

    #last name.
    LAST_NAME = cmd[4]
    LAST_NAME_PATTERN = r"^[a-zA-Z]{2,}$"
    matchLAST_NAME = re.search(LAST_NAME_PATTERN, LAST_NAME)

    while matchLAST_NAME == None:
        NEW_LAST_NAME = str(input("try again. enter last name: "))
        matchLAST_NAME = re.search(LAST_NAME_PATTERN, NEW_LAST_NAME)

    if " " in LAST_NAME:
        LAST_NAME = LAST_NAME.replace(" ","+")

    #natural numbers
    SEASON_WIN = cmd[5]
    SEASON_WIN_PATTERN = r"[0-9]{1,}"
    matchSEASON_WIN = re.search(SEASON_WIN_PATTERN, SEASON_WIN)

    while matchSEASON_WIN == None:
        NEW_SEASON_WIN = str(input("try again. enter season win (number greater than zero): "))
        matchSEASON_WIN = re.search(SEASON_WIN_PATTERN, NEW_SEASON_WIN)

    #natural numbers
    SEASON_LOSS = cmd[6]
    SEASON_LOSS_PATTERN = r"[0-9]{1,}"
    matchSEASON_LOSS = re.search(SEASON_LOSS_PATTERN, SEASON_LOSS)

    while matchSEASON_LOSS == None:
        NEW_SEASON_LOSS = str(input("try again. enter season loss (number greater than zero): "))
        matchSEASON_LOSS = re.search(SEASON_LOSS_PATTERN, NEW_SEASON_LOSS)

    #natural numbers
    PLAYOFF_WIN = cmd[7]
    PLAYOFF_WIN_PATTERN = r"[0-9]{1,}"
    matchPLAYOFF_WIN = re.search(PLAYOFF_WIN_PATTERN, PLAYOFF_WIN)

    while matchPLAYOFF_WIN == None:
        NEW_PLAYOFF_WIN = str(input("try again. enter playoff win (number greater than zero): "))
        matchPLAYOFF_WIN = re.search(PLAYOFF_WIN_PATTERN, NEW_PLAYOFF_WIN)

    #natural numbers
    PLAYOFF_LOSS = cmd[8]
    PLAYOFF_LOSS_PATTERN = r"[0-9]{1,}"
    matchPLAYOFF_LOSS = re.search(PLAYOFF_LOSS_PATTERN, PLAYOFF_LOSS)

    while matchPLAYOFF_LOSS == None:
        NEW_PLAYOFF_LOSS = str(input("try again. enter playoff loss (number greater than zero): "))
        matchPLAYOFF_LOSS = re.search(PLAYOFF_LOSS_PATTERN, NEW_PLAYOFF_LOSS)

    #capital letters or numbers (3 characters)
    TEAM = cmd[9]
    TEAM_PATTERN = r"^[A-Z]{2,3}[0-9]?$"
    matchTEAM = re.search(TEAM_PATTERN, TEAM)

    while matchTEAM == None:
        NEW_TEAM = str(input("try again. enter team: "))
        matchTEAM = re.search(TEAM_PATTERN, NEW_TEAM)

    new_coach = Coaches(ID, SEASON, FIRST_NAME, LAST_NAME, SEASON_WIN, SEASON_LOSS, PLAYOFF_WIN, PLAYOFF_LOSS, TEAM)
    coachesArray.append(new_coach)

    print("\nThe following has been added to the coaches Array:")
    new_coach.print_coach()

# add a team to the teams.txt add_team takes ID, LOCATION, NAME, LEAGUE 
def add_team(teamsArray,cmd):
    ID = cmd[1]
    ID_PATTERN = r"^[A-Z0-9]{3}$"
    matchID = re.search(ID_PATTERN, ID)
    while matchID == None:
        NEW_ID = str(input("try again. enter team id (7 capital letters and 2 integers): "))
        matchID = re.search(ID_PATTERN, NEW_ID)

    LOCATION = cmd[2]
    LOCATION_PATTERN = r"^[a-zA-Z]{2,}$"
    matchLOCATION = re.search(LOCATION_PATTERN, LOCATION)
    while matchLOCATION == None:
        NEW_LOCATION = str(input("try again. enter team location: "))
        matchLOCATION = re.search(LOCATION_PATTERN, NEW_LOCATION)

    NAME = cmd[3]
    NAME_PATTERN = r"^[a-zA-Z]{2,}$"
    matchNAME = re.search(NAME_PATTERN, NAME)
    while matchNAME == None:
        NEW_NAME = str(input("try again. enter team location: "))
        matchNAME = re.search(NAME_PATTERN, NEW_NAME)

    LEAGUE = cmd[4]
    LEAGUE_PATTERN = r"^[A-Z]{1}$"
    matchLEAGUE = re.search(LEAGUE_PATTERN, LEAGUE)
    while matchLEAGUE == None:
        NEW_LEAGUE = str(input("try again. enter team league: "))
        matchLEAGUE = re.search(LEAGUE_PATTERN, NEW_LEAGUE)


    new_team = Teams(ID, LOCATION, NAME, LEAGUE)
    teamsArray.append(new_team)

    print("\nThe following has been added to the teams Array:")
    new_team.print_team()

    

#adding the coaches to an array
def load_coaches(coachArray,cmd):
    if len(coachArray) > 50: #arbitrary number limit of writes
        print("you already loaded coaches\n")
        return
        
    filename = cmd[1]

    i = 0
    with open(filename, "r") as file:
        next(file) #skips the first line
        for line in file:
            data = line.split(",")
            coach = Coaches(data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
            # add the coaches into the coachesArray.
            coachArray.append(coach)
            i+=1
            #print("coach", i, "added and loaded")
            #coach.print_coach()
    print()
    print("All",i , "coaches have been loaded into the coachArray\n")

def load_teams(teamArray,cmd):
    if len(teamsArray) > 50:  #arbitrary number limit of writes
        print("you already loaded teams\n")
        return

    filename = cmd[1]

    i = 0
    with open(filename, "r") as file:
        next(file) #skips first line
        for line in file:
            data = line.split(",")
            team = Teams(data[0], data[1], data[2], data[3])
            # add the coaches into the coachesArray.
            teamArray.append(team)
            i+=1
            #print("coach", i, "added and loaded")
            #team.print_team()
    print()
    print("All",i , "teams have been loaded into the teamsArray\n")


def print_coaches(coachesArray):
    if len(coachesArray) == 0:
        print("no coaches in the coachesArray")
        return

    print("ID\t\tSEASON\tFIRST_NAME\tLAST_NAME\tSEASON_WIN\tSEASON_LOSS\tPLAYOFF_WIN\tPLAYOFF_LOSS\tTEAM")
    for coach in coachesArray:
        coach.print_coach()
    print()


def print_teams(teamsArray):
    if len(teamsArray) == 0:
        print("no teams in the teamsArray")
        return
    print("TEAM\t\tLOCATION\t\tNAME\t\tLEAGUE")
    for team in teamsArray:
        team.print_team()
    print()

#Given a last name, print the information of coach(es) with that last name. 
#You should also add the locations (city) and names of all teams he coached.
def coaches_by_name(coachesArray, cmd):

    teamsCoached = list()

    if len(coachesArray) == 0:
        print("no coaches in the coachesArray")
        return

    lastName = cmd[1]
    print()

    #fotmating input when last Name is of the form Van+Dyke
    if "+" in lastName:
        lastName = lastName.replace("+","")

    #printing the coach information
    for coach in coachesArray:
        coachLastName = coach.LAST_NAME.replace(" ","")
        if lastName == coachLastName:
            coach.print_coach()
    

#Given a city name, print the information of teams in that city and 
#the names of all who coached teams in that city (each coach shown in a line.
def teams_by_city(coachesArray,teamsArray,cmd):

    if len(coachesArray) == 0:
        print("no coaches in the coachesArray")
        return

    if len(teamsArray) == 0:
        print("no teams in the teamsArray")
        return
    #printing the information about the teams in cityName
    cityName = cmd[1]
    print()
    for team in teamsArray:
        teamLocation = team.LOCATION.replace(" ","")
        if teamLocation == cityName:
            id = team.ID.replace(" ","")
            location = team.LOCATION
            name = team.NAME
            league = team.LEAGUE
            for coach in coachesArray:
                coachTeam = coach.TEAM.replace(" ","")
                if id.strip() == coachTeam.strip():
                    coachName = coach.LAST_NAME
                    print(id,location,name,league.strip(),coachName)
    

#print the name of the coach who has the most net wins in a season specified by the only argument.
#Note that the net wins should be calculated as (season_win - season_loss) + (playoff_win - playoff_loss).
def best_coach(coachesArray,cmd):
    coachesArray2 = list()
    if len(coachesArray) == 0:
        print("\nno coaches in the coachesArray")
        return
    for coach in coachesArray:
        coachSeason = coach.SEASON.replace(" ","")
        if coachSeason == cmd[1]:
            coachesArray2.append(coach)

    maxNetWins = 0
    for coach in coachesArray2:
        netWins = int(coach.SEASON_WIN) - int(coach.SEASON_LOSS) + int(coach.PLAYOFF_WIN) - int(coach.PLAYOFF_LOSS)
        if maxNetWins < netWins:
            maxNetWins = netWins
            best_coach = Coaches(coach.ID, coach.SEASON, coach.FIRST_NAME, coach.LAST_NAME, coach.SEASON_WIN, coach.SEASON_LOSS, coach.PLAYOFF_WIN, coach.PLAYOFF_LOSS, coach.TEAM)
    
    print(best_coach.FIRST_NAME,best_coach.LAST_NAME)

#print the info of coaches with the specified properties, which are given by the arguments in the following format: 
#field=VALUE where field represents the name of a search criterion and 
#'VALUE' is the value of that field you want the query results to match. Multiple fields can be used in the same query. 
#For example, a command "search_coaches first_name=John season_win=40" means 
#"finding all performance data of a coach with first name 'John' who had a seasonal win of 40". 
#Note that a meaningful field should match exactly one of the column names in the coaches table 
#(just ignore those that do not match any column names).

#A coach's last name can be two words with a space in between (e.g., van Gundy). Your code should be able to handle this. There will be testcases that search by such names. In order to not confuse your program, we will add a "+" sign between the two words of the last name in the testcases. For example,
def search_coaches(coachesArray, cmd):
    if len(coachesArray) == 0:
        print("no coaches in coachesArray")
        return

    if len(cmd) == 1:
        print("no arguments passed. try search_coaches first_name=Wes season_win=30")
        return

    commands = list()

    #ADDING ALL THE FIELD-VALUES TO THEN LOOP THROUGH THEM
    for i in range(1, len(cmd)):
        fieldValue = cmd[i].split("=")
        commands.append(fieldValue)


    #LOOPING THRU COACHES AND FIELDS TO MATCH THEM 
    for coach in coachesArray:
        count = 0
        for command in commands:    #command[0] -> field    #command[1] -> value
            if command[0] == "id":
                coachID = coach.ID.replace(" ","")
                if command[1] == coachID:
                    count += 1


            if command[0] == "season":
                coachSeason = coach.SEASON.replace(" ","")
                if command[1] == coachSeason:
                    count += 1


            if command[0] == "firstname":
                coachFirstName = coach.FIRST_NAME.replace(" ","")
                if command[1] == coachFirstName:
                    count += 1

            if command[0] == "lastname":
                lastName = command[1]
                coachLastName = coach.LAST_NAME.replace(" ","")
                if "+" in command[1]:
                    #to make the comparison I decided to remove " " and "+" from both and then compare
                    lastName = command[1].replace("+","")
                if lastName == coachLastName:
                    count += 1


            if command[0] == "season_win":
                coachSeasonWin = coach.SEASON_WIN.replace(" ","")
                if command[1] == coachSeasonWin:
                    count += 1


            if command[0] == "season_loss":
                coachSeasonLoss = coach.SEASON_LOSS.replace(" ","")
                if command[1] == coachSeasonLoss:
                    count += 1


            if command[0] == "playoff_win":
                coachPlayoffWin = coach.PLAYOFF_WIN.replace(" ","")
                if command[1] == coachPlayoffWin[0:3]:
                    count += 1


            if command[0] == "playoff_loss":
                coachPlayoffLoss = coach.PLAYOFF_LOSS.replace(" ","")
                if command[1] == coachPlayoffLoss:
                    count += 1

            if command[0] == "team":
                coachTeam = coach.TEAM.replace(" ","")
                team = command[1].replace(" ","")
                #print(command[1] + "." + coachTeam)
                if team.strip() == coachTeam.strip():
                    count += 1

            if count == i:
                coach.print_coach()
    
main()