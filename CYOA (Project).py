import random, time

'''
Title: Choose-Your-Own-Adventure Project: Baseball Career Simulation
Description: It has been your dream since you were 8 that you want to play baseball at the highest level, the Major League Baseball (MLB). You've just finished highschool and this is where your career starts. Let's start by creating a player build.
Created By: Shiv Patel
Date Created: 04/04/2022
Date Last Modified: 15/04/2022
'''
 
# Significant Variable/Counter
newLine = "\n" # Newline character
count = 0 # Counter
draftImpact = 0 # Boolean/counter (Injury scenario)
playerSign = 0 # Boolean/counter (If player gets drafted)
agent = 0 # Boolean/counter (If player signs with agent)
 
# Story Title (Displayed by a FIGlet)
print ("|-------------------------------------------------------------------------------------------------------------------------|")
print ("| ____                         __      ______            ______  __                  ____    __                           |")                           
print ("|/\  _`\                      /\ \    /\__  _\          /\__  _\/\ \                /\  _`\ /\ \\                          |")                          
print ("|\ \ \L\ \    ___      __     \_\ \   \/_/\ \/   ___    \/_/\ \/\ \ \___      __    \ \,\L\_\ \ \___     ___   __  __  __ |") 
print ("| \ \ ,  /   / __`\  /'__`\   /'_` \     \ \ \  / __`\     \ \ \ \ \  _ `\  /'__`\   \/_\__ \\  \  _ `\  / __`\/\ \/\ \/\ \\|")
print ("|  \  \ \\ \ /\ \L\ \/\ \L\.\_/\ \L\ \     \ \ \/\ \L\ \     \ \ \ \ \ \ \ \/\  __/     /\ \L\ \ \ \ \ \/\ \L\ \ \ \_/ \_//|")
print ("|   \ \_\ \_\ \____/\ \__/.\_\ \___,_\     \ \_\ \____/      \ \_\ \ \_\ \_\ \____\    \ `\____\ \_\ \_\ \____/\ \___x___/|")
print ("|    \/_/\/ /\/___/  \/__/\/_/\/__,_ /      \/_/\/___/        \/_/  \/_/\/_/\/____/     \/_____/\/_/\/_/\/___/  \/__//__/ |")
print ("|-------------------------------------------------------------------------------------------------------------------------|")
                                                                                                                        
                                                                                                                        
# Creating the player
   # Player Name
print (newLine)
firstName = input("Please enter the first name of your character: ")
lastName = input("Please enter the last name of your character: ")
 
print (newLine)
print("Welcome", firstName, lastName +". Your journey to the Show starts now!")
 
   # Choosing a jersey number (Using while loop)
print (newLine)
print ("Time to choose a jersey number!")
 
jersey = int(input("Please enter a jersey number (Number MUST be between 00-99!): "))
while jersey < 0 or jersey > 99:
   print ("Invalid jersey number choice! Please try again!")
   jersey = int(input("Please enter a jersey number (Number MUST be between 0-99!): "))
 
   # Jersey (Output changes depending on input)
if jersey > 9:
   initial = (firstName [0] + lastName [0])
   print (newLine)
   print ("Here's a representation of how your jersey might look!")
   print ("  __   __")
   print (" /  `-'  \\")
   print ("/_| ", initial,     "|_\\")
   print("  | ",jersey,"|") 
   print("  |     |") 
   print("  |_____|")
 
else:
   initial = (firstName [0] + lastName [0])
   print ("Here's a representation of how your jersey might look!")
   print ("  __   __")
   print (" /  `-'  \\")
   print ("/_| ", initial,     "|_\\")
   print("  | ",jersey," |") 
   print("  |     |") 
   print("  |_____|")
 
               
# Player position (Choosing the position of player)
print (newLine)
print ("Here are your position options")
print ("------------------------------")
print (" 1. Pitcher", newLine, "2. Catcher", newLine, "3. Corner Infielder (1B/3B)", newLine, "4. Middle Infielder (2B/SS)", newLine,"5. Outfielder (LF/CF/RF)", newLine)
playerPosition = int(input("Please enter the position your character will play: "))
     
while playerPosition > 5:
   playerPosition = int(input("Please enter the position your character will play: "))
  
else:
  
   if playerPosition == 1:
       print (firstName, lastName, "will be a PITCHER!", newLine)
   if playerPosition == 2:
       print (firstName, lastName, "will be a CATCHER!", newLine)
   if playerPosition == 3:
       print (firstName, lastName, "will be a corner infielder!", newLine)
   if playerPosition == 4:
       print (firstName, lastName, "will be a middle infielder", newLine)
   if playerPosition == 5:
       print (firstName, lastName, "will be a outfielder!", newLine)
 
 
   # Player build (arc-type)
if playerPosition == 1:
   print ("Here are your pitch type options (make sure FB is first; FB is a go to pitch in baseball!!:)  ")
   print ("------------------------------")
   print (" FB. Fastball", newLine, "CB. Curveball", newLine, "SL. Slider", newLine, "CH. Change-up", newLine, "SP. Splitter", newLine, "CU. Cutter", newLine)
  
   pitchOne = input("Please select your first pitch: ")
   pitchTwo = input("Please select your first pitch: ")
   pitchThree = input("Please select your first pitch: ")
  
   while pitchOne.upper() != "FB" :
       print ("You must have a fastball as your go-to pitch... most essential pitch in today's game!")
       pitchOne = input("Please select your first pitch: ")
 
   else:
       print (firstName, lastName, "your 3 pitch types are:", pitchOne.upper(), pitchTwo.upper(), pitchThree.upper(), newLine)
 
else:
   print ("Here are your position options")
   print ("------------------------------")
   print ("1. Defence", "2. Offence", newLine)
   playerType = int(input("What is your primary focus on the field? "))
 
   if playerType == 1:
      print ("Solid! You prioritize defence.", newLine)
   if playerType == 2:
       print ("Solid! You prioritize offence.", newLine)
 
# Choosing a college/pathway - Pitcher Edition
print ("Okay, now that you're done with building a player, you will have to choose a college")
 
if playerPosition == 1:
   print ("Since you are a pitcher, these schools are interested in you!", newLine)
   print ("Here are your school options: ")
   print ("------------------------------")
   print ("1. Vanderbilt University (Nashville, Tennessee)", newLine, "2. University of Florida, (Gainesville, Florida)",newLine, "3. Stanford University (Stanford, California)", newLine, "4. I would like to skip college and attend", newLine)
 
   college = int(input("Which college would you like to attend? "))
 
   if college != 4:
       if college == 1:
           print (newLine)
           print ("You have committed to Vanderbilt University! Congratulations on becoming a Commodore!")
       if college == 2:
           print (newLine)
           print ("You have committed to the University of Florida! Congratulations on becoming a Gator!")
       if college == 3:
           print (newLine)
           print ("You have committed to Stanford University!")
 
   else:
       print ("You have decided to skip college and pursue either:")
       print (newLine)
       print (" 1. Train on your own", newLine, "2. Play overseas")
       altChoice = int(input("Which option would you like to do?"))
       count = 1
      
  
# Choosing a college/pathway - Position Player Edition
if playerPosition > 1:
   if playerType == 1:
       # College choices (If player arc-type is defence)
       print ("Since you are a position player who prioritized defence, these are your schooling options: ")
       print ("Here are your school options: ")
       print ("------------------------------")
       print (" 1. Vanderbilt University (Nashville, Tennessee)", newLine, "2. University of Mississippi, (Oxford, Mississippi)",newLine, "3. University of Michigan (Ann Arbor, Michigan)", newLine, "4. I would like to skip college and attend", newLine)
 
   else:
       # College choices (If player arc-type is offence)
       print ("Since you are a position player who prioritized offence, these are your schooling options: ")
       print ("Here are your school options: ")
       print ("------------------------------")
       print (" 1. Vanderbilt University (Nashville, Tennessee)", newLine, "2. University of California, Los Angeles, (Los Angeles, California)", newLine, "3. University of Texas-Austin (Austin, Texas))", newLine, "4. I would like to skip college and attend", newLine)
      
   college = int(input("Which option would you like to choose? "))
 
   if college != 4 and playerType == 1:
       if college == 1:
           print (newLine)
           print ("You have committed to Vanderbilt University! Congratulations on becoming a Commodore!")
       if college == 2:
           print (newLine)
           print ("You have committed to the University of Mississippi! Congratulations on becoming a Rebel!")
       if college == 3:
           print (newLine)
           print ("You have committed to the University of Michigan! Congratulations on becoming a Wolverine!")
 
   # Opting out of college pathway (Choosing to train on own or go overseas)
   if college == 4 and playerType == 1:
       print ("You have decided to skip college and pursue either:")
       print (" 1. Train on your own", newLine, "2. Play overseas")
       count = 1
       altChoice = int(input("Which option would you like to do?"))
      
   # Outputs for college choice and which arc-type is chosen by user
   if college != 4 and playerType == 2:
       if college == 1:
           print ("You have committed to Vanderbilt University! Congratulations on becoming a Commodore!")
       if college == 2:
           print ("You have committed to the University of California, Los Angeles! Congratulations on becoming a Bruin!")
       if college == 3:
           print ("You have committed to the University of Texas-Austin! Congratulations on becoming a Longhorn!")
 
   if college == 4 and playerType == 2:
       print ("You have decided to skip college and pursue either:")
       print (" 1. Train on your own", newLine, "2. Play overseas")
       count = 1
       altChoice = int(input("Which option would you like to do?"))
  
 
# Option 4 - Not attending college
if count == 1:
   if altChoice == 1:
       print ("Would you like to sign with an agent?")
       print (" 1. Yes (Ineligible to attend college)", newLine, "2. No, (College remains an option if you change your decision", newLine)
       agent = int(input("Please indicate if you would like to sign with an agent?"))
 
       if agent == 1:
           print ("You have decided to sign with an agent. You will be represented by Boras Corporation.")
       if agent == 2:
           print ("You have decided to not sign with an agent. You can continue to train on your own.")
          
   if altChoice == 2:
       print ("Since you have decided to play overseas, you will have to sign with an agent")
       print ("You have decided to sign with an agent. You will be represented by Boras Corporation. They will find you teams that you can possibly play for.")
 
# College season ("Simulated season at college")
 
if college < 4:
   print ("After your first college season, these are the stats you put up:", newLine)
   if playerPosition == 1:
       print (newLine)
      
       # College stats
      
       # Pitching stats
       era = random.randint(0, 100)
       era = era/9.9
       innings = random.randint (10, 150)
       games = random.randint (1, 20)
       wins = random.randint (1, games)
       loss = games - wins
       whip = random.randint (0, 3)
       whip = whip / 1.5
      
       print ("Earned Run Average (ERA): ",round(era,3))
       print ("Innings Pitched (IP): ",innings)
       print ("Games Played In (GP): ",games)
       print ("Wins:", wins)
       print ("Losses: ",loss)
       print ("Walks Plus Hits Per Inning Pitched (WHIP)",round(whip,4))
       print (newLine)
 
 
   if playerPosition > 1 and playerType == 1:
       # Defensive player stats (Lower offensive numbers)
       print (newLine)
       batting = random.randint(0, 300)
       batting = batting/1000
       hits = random.randint (10, 100)
       homerun = random.randint (0, 15)
       rbi = random.randint (1, 50)
       stolenbase = random.randint (1, 20)
       ops = random.randint (500, 800)
       ops = ops/1000
      
       print ("Batting Average (BA): ", round(batting,3))
       print ("Hit(s) (H): ",hits)
       print ("Homerun (s) (HR): ", homerun)
       print ("Runs Batted In (RBI): ", rbi)
       print ("Stolen Bases (SB): ",stolenbase)
       print ("On-Base Plus Slugging (OPS): ", round (ops, 3))
       print (newLine)
      
   if playerPosition > 1 and playerType == 2:
       # Offensive player stats
       print (newLine)
       batting = random.randint(0, 450)
       batting = batting/1000
       hits = random.randint (10, 125)
       homerun = random.randint (0, 25)
       rbi = random.randint (1, 85)
       stolenbase = random.randint (1, 10)
       ops = random.randint (700, 1100 )
       ops = ops/1000
      
       print ("Batting Average (BA): ", round(batting, 4))
       print ("Hit(s) (H): ",hits)
       print ("Homerun (s) (HR): ", homerun)
       print ("Runs Batted In (RBI): ", rbi)
       print ("Stolen Bases (SB): ",stolenbase)
       print ("On-Base Plus Slugging (OPS): ", round (ops, 4))
       print (newLine)
      
# Training on own (If a certain choice is picked)
if college == 4 and altChoice == 1:
   print ("You trained on your own for the past months and now it's your choice if you feel ready to declare for the MLB draft.")
  
# Overseas (If a certain choice is picked)
if college == 4 and altChoice == 2:
   print (newLine)
   print ("Your agent has found 3 teams to sign from: ", newLine)
   print (" 1. Nippon Professional Baseball - Tokyo Yakult Swallows (Tokyo, Japan)", newLine, "2. Frontier League - Schaumburg Boomers (Schaumburg, Illinois)", newLine, "3. KBO League - KT Wiz (Suwon, South Korea)", newLine)
  
   # Outcomes when attending overseas (depending on player arc-type)
   overseas = int(input("Which league, team, and location would you like to play for?"))
   if overseas == 1:
       print ("You joined the Nippon Professional Baseball league and played for the Tokyo Yakult Swallows!", newLine)
   if overseas == 2:
       print ("You joined the Frontier League and played for the Schaumburg Boomers!", newLine)
   if overseas == 3:
       print ("You joined the KBO League and played for the KT Wiz!", newLine)
 
   # Injury (if player chooses certain option)
   if playerPosition == 1:
       print ("But unfortunately, you were hurt for the entire season. During the first practice, you tore your elbow ligament, which required season ending surgery. This will heavily impact your draft status", newLine)
       draftImpact = 1
   else:
       if playerType == 1:
           print ("But unfortunately, you were hurt for the entire season. During the first preseason game, you were sprinting for a ball and felt a weird pop in your knee. It ended up being an ACL tear, which required season ending surgery. This will heavily impact your draft status.", newLine)        
           draftImpact = 1
       if playerType == 2:
           print ("After your first professional season, these are the stats you put up:", newLine)
           # Stats for overseas season
           batting = random.randint(0, 350)
           batting = batting/1000
           hits = random.randint (10, 155)
           homerun = random.randint (0, 35)
           rbi = random.randint (1, 95)
           stolenbase = random.randint (1, 5)
           ops = random.randint (750, 1100 )
           ops = ops/1000
      
           print ("Batting Average (BA): ", round(batting, 3))
           print ("Hit(s) (H): ",hits)
           print ("Homerun (s) (HR): ", homerun)
           print ("Runs Batted In (RBI): ", rbi)
           print ("Stolen Bases (SB): ",stolenbase)
           print ("On-Base Plus Slugging (OPS): ", round (ops, 3))
           print (newLine)
             
# Declaring for the MLB draft
print ("After a long time, time has come to make THE choice.", newLine)
print ("Would you like to declare for the upcoming MLB draft?", newLine)
print (" 1. Yes", newLine, "2. No", newLine)
draft = int(input("Is the answer yes or no? "))
 
# Outputs based on draft declaration
if draft == 1:
   print (newLine)
   print ("Great!", firstName, lastName, "you have declared for the upcoming MLB draft. You have been automatically been given an invite to the MLB Draft Combine! A place where you will be given one more chance to prove what you are all about! Good luck!")
if draft == 2:
   print (newLine)
   print ("That's fine!", firstName, lastName, "if that's what you feel is best, that is completely understandable!")
 
# MLB Combine (One last chance to showcase talents)
if draft == 1:
   print (newLine)
   if draftImpact == 1:
       print ("Due to your injury, your Combine performance wasn't the greatest. You are unlikely to get drafted in the first round, but the possibility of getting drafted is still in play.")
  
   else:
       print ("You had a great draft combine! Scouts were impressed with your performance and are expecting to see you get drafted in a top spot!")
 
# Salary Breakdown
   salary = 8500000
   print ("Prior to the MLB draft, understand the breakdown of the salary for each pick in the first round.")
   for i in range (1, 31):
       print ("Pick", str(i)+": ", "$"+str(salary), "USD.")
       print (newLine)
       salary = salary - 275000
       time.sleep (0.25)
  
# MLB Draft ("Simulated")
 
   print (newLine)
   print ("Welcome to the annual MLB Amateur Draft!.", newLine, "Today, many of the worlds top prospects will move onto new beginnings and start their journey to the Show. We wish all the athletes and families all the best!")
   print (newLine)
   if draftImpact == 0:
       draftPick = random.randint (1, 30)
   else:
       draftPick = random.randint (10, 50)
 
# Ending 1 - Undrafted (Depends on previous choices)
   if draft == 1:
       if draftPick > 30:
           print ("Unfortunately, you went undrafted. Though this is not the end of your story, this is just the beginning! Take all of this experience and come back stronger next year")
 
# Ending 2 - Drafted, not satisfied
       if draftPick < 31:
           print ("You were drafted at pick", draftPick, "this may not be where you expected yourself to be drafted, this is still great! Though would you like to settle at that pick and sign with the team, or try again next year, by re-entering the MLB draft.", newLine)
           print (" 1. Sign with the team", newLine, "2. Remain unsigned; Re-enter MLB draft next year", newLine)
           reenter = int(input("Would you like to sign with the team? "))
 
           if reenter == 2:
               print (newLine)
               print ("If you find that this is the best choice for you and your family, we understand.")
           else:
               playerSign = 1
 
# Ending 3 - Drafted, satisfied (Singing contract)
       if playerSign == 1:
           print (newLine)
           print ("Congratulations on being drafted at pick", draftPick)
# Signing a contract
           print (newLine)
           print ("Now, you will have to sign a contract with the team that chose you.")
          
           # Signing with agent (If agent was not signed with before)
           if agent == 1:
               print (newLine)
               print ("Your representation group, Boras Corp, will help you sign your first contract")
           else:
               print (newLine)
               print ("You do not have an agent to represent you.", newLine, "You will be represented by Rich Paul and Klutch Sports.")
 
           while i != draftPick:
               while i > draftPick:
                   i -= 1
               while i < draftPick:
                   i += 1
           else:
               salary = 8500000 - ((i-1) * 275000)
               print (newLine)
               print ("You have signed a 4 year $" + str(salary * 4),"USD contract! With an average of", (salary/4), "USD per year!", newLine)
               print ("Congratulations on your first MLB contract!", newLine)
 
               # First media conference
               print (newLine)
               print ("At your first press conference, you were asked by a reporter:", newLine)
               retirement = int(input("How many seasons do you plan to play? (Enter a number value): "))
 
               while retirement <= 0:
                   print ("HAHA! You cannot play a negative number or 0 number of years!")
                   retirement = int(input("How many seasons do you plan to play? (Enter a number value): "))
               else:
                   print ("You are currently 19 years of age... At the end of your career, you will be:", newLine)
                   print (19 + retirement, "years old!", newLine)
                   for i in range (1, retirement + 1):
                       print (newLine)
                       print ("Season:", i, "Age =", 19 + i, "\U0001F6A9")
                       time.sleep (0.25)
              
      
  
# Ending 4 - Deciding not to enter draft
else:
    print (newLine)
    print ("Well,", firstName, lastName, "it was a pleasure to write your story. Unfortunately you have decided to not declare for the MLB draft, but your journey doesn't end here!")
  
 
# Conclusion (Same for all)
print (newLine)
print ("Hope you had a good time reading and interacting with my story! Never give up and always strive for greatness (:")
