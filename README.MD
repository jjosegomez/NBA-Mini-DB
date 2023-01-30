# MINI NBA DATABASE
- In this project, I built a small database that stores data related to NBA coaches and teams. Users can send simple queries to this database, and add new data to the database. The database has two tables (or relations) - one for coaches and one for teams.


## Getting Started
- To run this project you need to type the follwing command

* ```~ python commands.py```

## Prerequisites
- Python 3
- No other dependancies are needed

## Usage
- Input the commands shown below to navigate throught the terminal app.

## Commands

1. add_coach: add a new record describing the performance of one coach in one season. It should have the following 9 arguments: ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM, the types of which should match the schema of relation "coaches" mentioned above. Note the data file contains another field named yr_order but you should not include it in your database

2. add_team: add a new record with one team's basic information. It should be followed by the following 4 arguments: ID LOCATION NAME LEAGUE, the types of which should match the schema of the "teams" table;

3. load_coaches : bulk load of multiple coach/season records from a file specified by the only argument of the command. Note that the file stores each record in one line of text, and different fields of the line/record are separated by commas. In our sample files, you may find empty attribute values (nothing in between two commas) and you should still load that line into your database instead of rejecting it.

4. load_teams : bulk load of multiple team records from a file specified by the only argument of the command. Records in such files are organized in the same way as in those for load_coaches.

5. print_coaches: print a list of all coaches, with info about one coach's performance in one season in a line;

6. print_teams: print a list of all teams, with info about one team per line;

7. coaches_by_name : given a last name, print the information of coach(es) with that last name. You should also add the locations (city) and names of all teams he coached;

8. teams_by_city : given a city name, print the information of teams in that city and the names of all who coached teams in that city (each coach shown in a line);

9. best_coach: print the name of the coach who has the most net wins in a season specified by the only argument. Note that the net wins should be calculated as (season_win - season_loss) + (playoff_win - playoff_loss).

10. search_coaches: print the info of coaches with the specified properties, which are given by the arguments in the following format: field=VALUE where field represents the name of a search criterion and 'VALUE' is the value of that field you want the query results to match. Multiple fields can be used in the same query. For example, a command "search_coaches first_name=John season_win=40" means "finding all performance data of a coach with first name 'John' who had a seasonal win of 40". Note that a meaningful field should match exactly one of the column names in the coaches table (just ignore those that do not match any column names).

A coach's last name can be two words with a space in between (e.g., van Gundy). Your code should be able to handle this. There will be testcases that search by such names. In order to not confuse your program, we will add a "+" sign between the two words of the last name in the testcases. For example,

## Author
Juan J Gomez Medina U70962227