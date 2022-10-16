# https://www.fia.com/regulation/category/110     link to the f1 sporting regulations page
# this calculator isn't accurate to the rules but was a fun little project to get back into programing. 
fullpoints = [25,18,15,12,10,8,6,4,2,1]

# gather race details 
totallaps = int(input('How many laps is the race? '))
lapscompleted = int(input('How many laps were completed? '))
place = int(input('What place did your driver get? '))
fastestLap = input('Did your driver get the fastest lap? y or n: ')
percentcompleted = (lapscompleted/totallaps)*100

#determine points that should be received

def pointsreceived(totallaps, lapscompleted, place, percentcompleted):
    points = 0
    if fastestLap == 'y':
        points += 1
    if lapscompleted < 2:
        points = 0
    elif lapscompleted/totallaps < .75:
        points += (fullpoints[place-1]/2)
    elif lapscompleted/totallaps == 1:
        points += fullpoints[place-1]
    return points
        

#print results
print(F'Your driver received {pointsreceived(totallaps, lapscompleted, place, percentcompleted)} points.')
