#------top 100 songs-------
#student ID: 301558325
#Name: Xu Han 
# Cmpt 120 online 
#==================== PART 1 ==================

love_counter = 0      #counts how many songs have the word live
top_two_counter = 0   
top_two = ""
artist_name = ''
advanced_rank = 0
average_weeks_on_board = 0
total_weeks = 0
    
file = open("charts.csv")

for line in file:
    songlist = line.split(",")  
    date = songlist[0]
    rank = songlist[1]
    song = songlist[2]
    artist = songlist[3]
    last_week = songlist[4]
    peak_rank = songlist[5]
    weeks_on_board = songlist[6]

    #---------- PT:1 'Love' in song ----------
    
    if 'Love' in song or 'love' in song:
        love_counter = love_counter + 1

    #---------- PT:1 top rank songs ----------

    if rank == '1' or rank == '2':
        top_two_counter = top_two_counter + 1
        top_two = top_two + song + ('\n')
        
    #---------- PT:1 'A' named artists ----------
    
    if artist[0] == 'A' or artist[0] == 'a':
        artist_name = artist_name + artist + ('\n')

    #---------- PT:1 rank better than last week ----------
  
    if rank < last_week: 
        advanced_rank = advanced_rank + 1

    #---------- PT:1 avg wks on board ----------

    weeks_on_board = int(weeks_on_board)
    average_weeks_on_board = average_weeks_on_board + weeks_on_board
    total_weeks = total_weeks + 1
    average = average_weeks_on_board/total_weeks

    #---------- PART 1 PRINT AND RUN -----------

print('\n' + "Hello and welcome to the Billboard top 100 app !" + "\n")
print("PART 1")
print("=======" + "\n")
print("Number songs containing the word 'love':", love_counter , '\n')
print('Songs names in rank positions 1 or 2:', top_two_counter ,'\n' + top_two)
print("Artists names starting with 'A':" ,"\n" + artist_name)
print("Songs advancing in rank wrt previous week:" ,advanced_rank ,"\n")
print("Average weeks on board all songs:",round(average,2) , '\n')
print("------------ END OF PART 1 ------------", '\n')


#==================== PART 2  ==================

print("PART 2")
print("=======" + "\n")
print('First query: Individual artist songs' , '\n') 

#---------- PT:2 artist name lookup ----------

file.seek(0)
x = 0
true = 0
for line in file:
    songlist = line.split(",")  
    date = songlist[0]
    rank = songlist[1]
    song = songlist[2]
    artist = songlist[3]
    last_week = songlist[4]

    if x == 0:
        ask = input("Artist name (may be part of the name) --> ")
        ask = ask.strip(',.?! ')
        print('\n'+"{:<20}{:<20}{:<20}{:<10}{:<2}".format('Artist','Song',"Date",'Rank',"Previous rank"))  
        x = x + 1
    if x >= 1:
        lower_artist = artist.lower()
        ask = ask.lower()
        if ask in lower_artist:  
           print("{:<20} {:<20} {:<20} {:<10} {:<2}".format(artist,song,date,rank,last_week))  
           true += 1
if true == 0:
    print("There is no such artist in the file")

#------------- Pt:2 artist lookup ------------

print('\n' + "Second query: Songs and weeks on board")
file.seek(0)
y = 0
t = True
for line in file:
    songlist = line.split(",")  
    date = songlist[0]
    song = songlist[2]
    weeks_on_board = songlist[6]
    if y == 0:
        ask2 = input('Song title (may be part of the title) --> ')
        ask2 = ask2.strip(',.?! ')
        print('\n' + "{:<20} {:<20} {:<20}".format('Requested Song',"Date",'Weeks on board'))  
        y = y + 1
    if y == 1:
        lower_song = song.lower()
        ask2 = ask2.lower()
        if ask2 in lower_song: 
            list = song 
            print("{:<20} {:<20} {:<20}".format(song, date, weeks_on_board), '\n') 
            t = False
            break            
if t == True:
    print("There is no such song in the file")
number = weeks_on_board
number = int(number)

#-------- PT:2 songs that ranked higher ------ 
    
file.seek(0)
yes = False
print('--------------------')
print("Songs with more weeks on board than the requested song" + '\n')
print("{:<20} {:<20} {:<20}".format('Song', 'Date', "Extra weeks on board"))
if t == False:
    for line in file:
        songlist = line.split(",")  
        date = songlist[0]
        song = songlist[2]
        weeks = songlist[6]
        
        weeks = int(weeks)
        if number < weeks:
            yes = True
            if yes == True:
                weeks = weeks - number
                print("{:<20} {:<20} {:<20}".format(song, date, weeks))   
elif yes == False:
    pass

print('\n' +  "Bye! End of app!")     