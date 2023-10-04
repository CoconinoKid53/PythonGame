print('Welcome to Suspense Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions=7

# The idea that helped me come with this adventure game of loving watch suspense movies
if answer.lower()=='yes':
    answer=input('Question 1: you have two paths one rocky and one smooth which do you choose?')
    if answer.lower()=='rocky':
        score+=1
        print('correct you found your dream car with the keys in the ignition full of gas')
    else:
        print('Wrong answer now you arrived at broken down house')



        answer=input('Question 2: You drive off to paradise or investigate the broken down house?')
    if answer.lower()=='paradise':
        score+=1
        print('correct you investigate the house fall down unconcious and awake to find yourself in your bed')
    else:
        print('Wrong you get a flat tire and arrive at a shady hotel and head on in')




        answer=input('Question 3: Look around your suroundings what do you see and hear in both endings?')
    if answer.lower()=='Happy':
        score+=1
        print('correct you found it was all a nightmare with the abandoned house and awake happy')
    else:
        print('wrong you get checked in and told after trying to leave Welcome to the Hotel California')



        answer=input('question 4: Welcome to the new suspense stuck in haunted house or locked in costco')
    if answer.lower()=='Haunted':
        score+=1
        print ('Correct you get locked in costco having free range of snacks')
    else:
        print('wrong locked in haunted house complete darkness and unexpected jumpscares every hour')

        answer=input('Question 5: in costco you hear things do you investigate or found light and escape haunted house?')
    if answer.lower()=='escape':
        score+=1
        print('correct you found an escape head back home and have a good nights rest')
    else:
        print('wrong hearing footsteps into the night and you go to hide in the freezer but the door shuts')



        answer=input('question 6: go through the hole in the wall and escape or unexpectedly awake terrified?')
    if answer.lower()=='Terrified':
        score+=1
        print('correct you found yourself not in the right house to actually sweat to find in another haunted house')
    else:
        print('wrong you escaped the freezer to hear freeze and end up in the back of a cop car for tresspassing')




        answer=input('question 7: after heading to jail cop car is abdcuted you escape or call your parents and head home?')
        if answer.lower()=='abducted':
            score+=1
        print('correct you came to find out it was all a nightmare')
else:
    print('wrong you cant seem to make sense if it was real or not')






    # different set of code that was difficult to continue the adventure game
    print('Thank you for playing my goblins and ghouls you attempted',score,'questions correctly!')
    mark=(score/total_questions)*100
    print('Marks obtained:',mark)
    print('Happy Halloween')



  # make a new situation to every story just make it more unpredicatble like life