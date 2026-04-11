# Quiz game:-

print('welcome to Quiz game...')
score = 0
print('Q1. what is the first alphabet of english ?\n A) b B)g \n C)a D)i')
ans = input('enter your answer..')

if ans =='c':
    score= score+5
print('Q2. what is the name of  national animal ?\n A) tiger B)lion \n C)elephant D)deer')
ans1 = input('enter your answer..')
if ans1=='a':
    score=score+5
print('Q3. what is the name of  national bird ?\n A) Hen B)peacock \n C)owl D)ostrich')
ans1 = input('enter your answer..')
if ans1=='b':
    score=score+5
print('Q4. In which direction does the sun rise ?\n A) west B)north\n C)east D)south')
ans1 = input('enter your answer..')
if ans1=='c':
    score=score+5  
print('Q5. what is the name of national flower ?\n A) rose B)sunflower\n C)lily D)lotus')
ans1 = input('enter your answer..')
if ans1=='d':
    score=score+5
print('Q6. what is the capital of india ?\n A) haryana B)New Delhi\n C)uttar pradesh D)kashmir')
ans1 = input('enter your answer..')
if ans1=='b':
    score=score+5    
print('you have scored',score)
if score == 30:
    print("congress your first postion")
elif score==25:
    print("congress your second postion")
elif score==20:
    print("congress your third postion")   
else:
    print("better luck next time")