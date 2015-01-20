<<<<<<< HEAD
'''
bronze = False
silver = False
gold = False
platinum = False
completed = [bronze, silver, gold, platinum]
values = ['bronze', 'silver', 'gold', 'platinum']
medals = [0,10,0,0]
score = 6
played = 1


def achievement_first_time(played):
    achievement_played = False
    while not achievement_played:
        if played == 1:
            achievement_played = 'Well done for completing your first game.'
            return achievement_played
        if played == 50:
            achievement_played = 'Well done for completing your 50th game.'
            return achievement_played

def achievement_medal_champ(medals, values, completed):
    counter = 0
    for i in medals:
        if i == 10 and completed[counter] == False:
            string = 'you have won the %s medal champion achievement for gettign 10 %s medals' % (values[counter], values[counter])
            completed[counter] = True
            return string, completed
        else:
            return '', completed
        counter +=1
'''
        
def award(score):
	if score < 5:
		award = 'bronze'
	if score >= 5 and score < 8:
		award = 'silver'
	if score >= 8 and score < 10:
		award = 'gold'
	if score >= 10:
		award = 'platinum'
	return award

def medal_addition(score, medals):
    medal_recieved = award(score)
    if medal_recieved == 'bronze':
        medals[0] = medals[0] + 1
    if medal_recieved == 'silver':
        medals[1] = medals[1] + 1
    if medal_recieved == 'gold':
        medals[2] = medals[2] + 1
    if medal_recieved == 'platinum':
        medals[3] = medals[3] + 1
    return medals
        
'''calculations = medal_addition(score, medals)
medal_achievement = achievement_medal_champ(medals, values, completed)
times_played_achievement = achievement_first_time(played)
completed = medal_achievement[1]'''


=======
__author__ = 'matthewcrown'
#To change this template use Tools | Templates.
>>>>>>> 808a0b04f2f9f80a72f5c5938afae6968e3da929
