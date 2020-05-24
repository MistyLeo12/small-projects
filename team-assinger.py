"""
Program I made to randomly partner people together each week to come up with a spotify playlist together 
for an on campus publication that I was the Audio/Video Editor for. 

Potential: Adding a 3rd party api that would notify each person would have been a next step which would
have been useful--also sending reminder notifications to that weeks members

"""
import random 

team_list = ["Nathan","Evan","Nina","John","Andy","Avery","Drew","Nick","Ryan","Rachel","Zoe","Gabriel"]
partners = {}

while len(team_list) > 1:
    x1 = random.randrange(0, len(team_list))
    person1 = team_list.pop(x1)

    x2 = random.randrange(0, len(team_list))
    person2 = team_list.pop(x2)
#After randomly popping people from team_list, we assign person1 to be the key and person2 to be val in the dict
    partners[person1] = person2

week_number = 1

for key, value in partners.items():
    print("Week {}: {} and {}".format(week_number, key, value))
    week_number += 1