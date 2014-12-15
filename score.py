score1 = int(input('第一次考試成績\n'))
score2 = int(input('第二次考試成績\n'))
score3 = int(input('第三次考試成績\n'))
S = sorted([score1,score2,score3])
average = (S[0]*0.2+S[1]*0.3+S[2]*0.5)

print (average)
