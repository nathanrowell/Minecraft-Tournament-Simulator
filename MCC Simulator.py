from dataclasses import dataclass
import random
import time
import math
import operator
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
@dataclass
class Player:
    name: str
    skill: int
    coins: int
    random: int
    identifier: int
    team: int
    kills: int
    total_coins: int
    color: str
@dataclass
class Team:
    number: int 
    skill: int 
    random: int
    coins: int
    total_coins: int
    name: str
    color: str
team_1x = Team(1,50,0,0,0,"Red Rabbits","RED")
team_2x = Team(2,50,0,0,0,"Orange Ocelots","YELLOW")
team_3x = Team(3,50,0,0,0,"Yellow Yaks","LIGHTYELLOW_EX")
team_4x = Team(4,50,0,0,0,"Lime Llamas","LIGHTGREEN_EX")
team_5x = Team(5,50,0,0,0,"Green Geckos","GREEN")
team_6x = Team(6,50,0,0,0,"Cyan Coyotes","CYAN")
team_7x = Team(7,50,0,0,0,"Aqua Axolotls","LIGHTCYAN_EX")
team_8x = Team(8,50,0,0,0,"Blue Bats","BLUE")
team_9x = Team(9,50,0,0,0,"Purple Pandas","MAGENTA")
team_10x = Team(10,50,0,0,0,"Pink Parrots","LIGHTRED_EX")
teams = [team_1x, team_2x,team_3x,team_4x,team_5x,team_6x,team_7x,team_8x,team_9x,team_10x]
player_1= Player('player1',80,0,0,0,1,0,0,'RED')
player_2= Player('player2',80,0,0,0,1,0,0,'RED')
player_3= Player('player3',60,0,0,0,1,0,0,'RED')
player_4= Player('player4',40,0,0,0,1,0,0,'RED')
player_5= Player('player5',80,0,0,0,2,0,0,'YELLOW')
player_6= Player('player6',40,0,0,0,2,0,0,'YELLOW')
player_7= Player('player7',60,0,0,0,2,0,0,'YELLOW')
player_8= Player('player8',60,0,0,0,2,0,0,'YELLOW')
player_9= Player('player9',100,0,0,0,3,0,0,'LIGHTYELLOW_EX')
player_10= Player('player10',80,0,0,0,3,0,0,'LIGHTYELLOW_EX')
player_11= Player('player11',40,0,0,0,3,0,0,'LIGHTYELLOW_EX')
player_12= Player('player12',40,0,0,0,3,0,0,'LIGHTYELLOW_EX')
player_13= Player('player13',100,0,0,0,4,0,0,'LIGHTGREEN_EX')
player_14= Player('player14',80,0,0,0,4,0,0,'LIGHTGREEN_EX')
player_15= Player('player15',60,0,0,0,4,0,0,'LIGHTGREEN_EX')
player_16= Player('player16',20,0,0,0,4,0,0,'LIGHTGREEN_EX')
player_17= Player('player17',100,0,0,0,5,0,0,'BLUE')
player_18= Player('player18',100,0,0,0,5,0,0,'BLUE')
player_19= Player('player19',40,0,0,0,5,0,0,'BLUE')
player_20= Player('player20',20,0,0,0,5,0,0,'BLUE')
player_21= Player('player21',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
player_22= Player('player22',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
player_23= Player('player23',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
player_24= Player('player24',20,0,0,0,6,0,0,'LIGHTCYAN_EX')
player_25= Player('player25',100,0,0,0,7,0,0,'CYAN')
player_26= Player('player26',60,0,0,0,7,0,0,'CYAN')
player_27= Player('player27',60,0,0,0,7,0,0,'CYAN')
player_28= Player('player28',20,0,0,0,7,0,0,'CYAN')
player_29= Player('player29',100,0,0,0,8,0,0,'MAGENTA')
player_30= Player('player30',80,0,0,0,8,0,0,'MAGENTA')
player_31= Player('player31',60,0,0,0,8,0,0,'MAGENTA')
player_32= Player('player32',20,0,0,0,8,0,0,'MAGENTA')
player_33= Player('player33',80,0,0,0,9,0,0,'LIGHTRED_EX')
player_34= Player('player34',60,0,0,0,9,0,0,'LIGHTRED_EX')
player_35= Player('player35',60,0,0,0,9,0,0,'LIGHTRED_EX')
player_36= Player('player36',40,0,0,0,9,0,0,'LIGHTRED_EX')
player_37= Player('player37',60,0,0,0,10,0,0,'GREEN')
player_38= Player('player38',60,0,0,0,10,0,0,'GREEN')
player_39= Player('player39',60,0,0,0,10,0,0,'GREEN')
player_40= Player('player40',60,0,0,0,10,0,0,'GREEN')
end_round = 0
team_1 = [player_1,player_2,player_3,player_4]
team_2 = [player_5,player_6,player_7,player_8]
team_3 = [player_9,player_10,player_11,player_12]
team_4 = [player_13,player_14,player_15,player_16]
team_5 = [player_17,player_18,player_19,player_20]
team_6 = [player_21,player_22,player_23,player_24]
team_7 = [player_25,player_26,player_27,player_28]
team_8 = [player_29,player_30,player_31,player_32]
team_9 = [player_33,player_34,player_35,player_36]
team_10 = [player_37,player_38,player_39,player_40]
def speed():
    while 2 != 3:
        speed = input("Put Speed to FAST,REGULAR,SLOW,INSTANT\n")
        if speed == "FAST":
            return 0.5
        if speed == "REGULAR":
            return 1
        if speed == "SLOW":
            return 1.5
        if speed == "INSTANT":
            return 0
    return speed
timer = speed()
teams = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10]
playing = [player_1	, player_2,	player_3	,player_4,	player_5	,player_6,	player_7,	player_8,	player_9,	player_10,
            player_11,	player_12,	player_13,	player_14,	player_15,	player_16,	player_17,	player_18,	player_19,	player_20,
            player_21,	player_22,	player_23,	player_24,	player_25,	player_26,	player_27,	player_28,	player_29,	player_30,
            player_31,	player_32,	player_33,	player_34,	player_35,	player_36,	player_37,	player_38,	player_39,	player_40]

def RSR(players,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    minimum = 100000
    placement = 40
    last_place = player_0
    end = []
    for player in players:
        count = count + 1
    count2 = count
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill) + random.randint(1,players[index].skill)
            index = index + 1
        if count2 == 10:
            for player in players:
                player.coins = player.coins + 63
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+63🪙 ]   " + "\n")
            placement = placement - 1
        elif count2 < 10 and count2 >= 4:
            for player in players:
                player.coins = player.coins + 9
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+9🪙 ]   " + "\n")
            placement = placement - 1
        elif count2 == 2 or count2 ==3:
            for player in players:
                player.coins = player.coins + 17
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+17🪙 ]   " + "\n")
            placement = placement - 1
        elif count2 == 1:
            for player in players:
                player.coins = player.coins + 29
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+29🪙 ]   " + "\n")
            placement = placement - 1
        elif count2 == 40:
            for player in players:
                player.coins = player.coins + 0
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+3🪙 ]   " + "\n")
            placement = placement - 1
        else:
            for player in players:
                player.coins = player.coins + 3
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+3🪙 ]   " + "\n")
            placement = placement - 1
        index3 = 0
        for player in players:
            if player.name == last_place.name:
                end.append(players[index3])
                players.pop(index3)
            index3 = index3 + 1
            
        minimum = 10000
        index3 = 0
        index = 0
        index2 = index2 + 1
        count2 = count2 - 1
        #normally 0.5
        time.sleep(timer*0.5)
    
    sorted = []
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    '''for players in final:
        print(players.coins)
    for players in final:
        print(players.name)'''
    roundsummary = ''
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 2:
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
    if round == 3:
        for players in final:
            roundsummary += str(players.coins) + "\n"
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")

        





    return final,roundsummary
    
"""def team_total(total,multiplier,teams):
    team_1 = 0
    team_2 = 0
    team_3 = 0
    team_4 = 0
    team_5 = 0
    team_6 = 0
    team_7 = 0
    team_8 = 0
    team_9 = 0
    team_10 = 0
    for parts in total:
        if parts.team == 1:
            team_1 = team_1 + parts.coins
        if parts.team == 2:
            team_2 = team_2 + parts.coins
        if parts.team == 3:
            team_3 = team_3 + parts.coins
        if parts.team == 4:
            team_4 = team_4 + parts.coins
        if parts.team == 5:
            team_5 = team_5 + parts.coins
        if parts.team == 6:
            team_6 = team_6 + parts.coins
        if parts.team == 7:
            team_7 = team_7 + parts.coins
        if parts.team == 8:
            team_8 = team_8 + parts.coins
        if parts.team == 9:
            team_9 = team_9 + parts.coins
        if parts.team == 10:
            team_10 = team_10 + parts.coins
    team_1 = team_1 * multiplier
    team_2 = team_2 * multiplier
    team_3 = team_3 * multiplier
    team_4 = team_4 * multiplier
    team_5 = team_5 * multiplier
    team_6 = team_6 * multiplier
    team_7 = team_7 * multiplier
    team_8 = team_8 * multiplier
    team_9 = team_9 * multiplier
    team_10 = team_10 * multiplier
    print("Team 1 Points: " + str(team_1))
    print("Team 2 Points: " + str(team_2))
    print("Team 3 Points: " + str(team_3))
    print("Team 4 Points: " + str(team_4))
    print("Team 5 Points: " + str(team_5))
    print("Team 6 Points: " + str(team_6))
    print("Team 7 Points: " + str(team_7))
    print("Team 8 Points: " + str(team_8))
    print("Team 9 Points: " + str(team_9))
    print("Team 10 Points: " + str(team_10))
    print(math.trunc(team_1))
    print(math.trunc(team_10))
    print(math.trunc(team_2))
    print(math.trunc(team_3))
    print(math.trunc(team_4))
    print(math.trunc(team_5))
    print(math.trunc(team_6))
    print(math.trunc(team_7))
    print(math.trunc(team_8))
    print(math.trunc(team_9))
    for team in teams:
        if team.number == 1:
            team.total_coins += team_1
        if team.number == 2:
            team.total_coins += team_2
        if team.number == 3:
            team.total_coins += team_3
        if team.number == 4:
            team.total_coins += team_4
        if team.number == 5:
            team.total_coins += team_5
        if team.number == 6:
            team.total_coins += team_6
        if team.number == 7:
            team.total_coins += team_7
        if team.number == 8:
            team.total_coins += team_8
        if team.number == 9:
            team.total_coins += team_9
        if team.number == 10:
            team.total_coins += team_10"""


def team_total(total,teams,multiplier,end_round):
    @dataclass 
    class finalTeam:
        coins: int
        name: str
        color: str
    team_1 = finalTeam(0,"Red Rabbits","RED")
    team_2 = finalTeam(0,"Orange Ocelots","YELLOW")
    team_3 = finalTeam(0,"Yellow Yaks","LIGHTYELLOW_EX")
    team_4 = finalTeam(0,"Lime Llamas","LIGHTGREEN_EX")
    team_5 = finalTeam(0,"Green Geckos","GREEN")
    team_6 = finalTeam(0,"Cyan Coyotes","CYAN")
    team_7 = finalTeam(0,"Aqua Axolotls","LIGHTCYAN_EX")
    team_8 = finalTeam(0,"Blue Bats","BLUE")
    team_9 = finalTeam(0,"Purple Pandas","MAGENTA")
    team_10 = finalTeam(0,"Pink Parrots","LIGHTRED_EX")
    for people in playing:
        people.total_coins += people.coins
        people.coins = 0
    for parts in total:
        if parts.team == 1:
            team_1.coins = team_1.coins + parts.coins
        if parts.team == 2:
            team_2.coins = team_2.coins + parts.coins
        if parts.team == 3:
            team_3.coins = team_3.coins + parts.coins
        if parts.team == 4:
            team_4.coins = team_4.coins + parts.coins
        if parts.team == 5:
            team_5.coins = team_5.coins + parts.coins
        if parts.team == 6:
            team_6.coins = team_6.coins + parts.coins
        if parts.team == 7:
            team_7.coins = team_7.coins + parts.coins
        if parts.team == 8:
            team_8.coins = team_8.coins + parts.coins
        if parts.team == 9:
            team_9.coins = team_9.coins + parts.coins
        if parts.team == 10:
            team_10.coins = team_10.coins + parts.coins
    team_1.coins = team_1.coins * multiplier
    team_2.coins = team_2.coins * multiplier
    team_3.coins = team_3.coins * multiplier
    team_4.coins = team_4.coins * multiplier
    team_5.coins = team_5.coins * multiplier
    team_6.coins = team_6.coins * multiplier
    team_7.coins = team_7.coins * multiplier
    team_8.coins = team_8.coins * multiplier
    team_9.coins = team_9.coins * multiplier
    team_10.coins = team_10.coins * multiplier
    if end_round == 3:
        for team in teams:
            if team.number == 1:
                team.total_coins += team_1.coins
            if team.number == 2:
                team.total_coins += team_2.coins
            if team.number == 3:
                team.total_coins += team_3.coins
            if team.number == 4:
                team.total_coins += team_4.coins
            if team.number == 5:
                team.total_coins += team_5.coins
            if team.number == 6:
                team.total_coins += team_6.coins
            if team.number == 7:
                team.total_coins += team_7.coins
            if team.number == 8:
                team.total_coins += team_8.coins
            if team.number == 9:
                team.total_coins += team_9.coins
            if team.number == 10:
                team.total_coins += team_10.coins
    sort_list = [team_1,team_10,team_2,team_3,team_4,team_5,team_6,team_7,team_8,team_9]
    sorted_list = sorted(sort_list, key=operator.attrgetter('coins'))
    sorted_list.reverse()
    for teamed in sorted_list:
        print(getattr(Back, teamed.color)  + teamed.name + Style.RESET_ALL + " Points: " + Style.BRIGHT + Back.BLACK + str(math.trunc(teamed.coins)))
    for teamed in sort_list:
        print(math.trunc(teamed.coins))
    sorted_y = sorted(total, key=operator.attrgetter('coins'))
    sorted_y.reverse()
    counted = 1
    print("Top 5 Players:")
    for people in sorted_y:
        if counted < 6:
            print(Style.BRIGHT + str(counted) + ": " + Style.RESET_ALL +  getattr(Fore, people.color) + people.name + " " + str(math.trunc(people.coins)))
        counted += 1
    
teamsCompeting = []
def SG(teams):

    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    player_00 = Player("null",0,0,0,0,0,0,0,"RED")
    player_000 = Player("null",0,0,0,0,0,0,0,"RED")
    player_0000 = Player("null",0,0,0,0,0,0,0,"RED")
    player_100 = Player("null",0,0,0,0,0,0,0,"RED")
    player_1000 = Player("null",0,0,0,0,0,0,0,"RED")
    first_place = Player("null",0,0,0,0,0,0,0,"RED")
    killed = []
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    indexTeam = 0
    totalTeam = 10
    TeamTotal1 = 0
    TeamTotal2 = 0
    Decider = 0
    minimum = 100000
    leftOn1 = 4
    leftOn2 = 4 
    leftOn3 = 4 
    leftOn4 = 4
    leftOn5 = 4
    leftOn6 = 4
    leftOn7 = 4
    totalKills = 0
    leftOn8 = 4
    leftOn9 = 4
    leftOn10 = 4
    TeamsIn = 10
    TeamBattling1 = 0
    TeamBattling2 = 0
    TeamPlacement = 0
    TeamPlacement10 = 0
    TeamPlacement1 = 0
    TeamPlacement2 = 0
    TeamPlacement3 = 0
    TeamPlacement4 = 0
    TeamPlacement5 = 0
    TeamPlacement6 = 0
    TeamPlacement7 = 0
    TeamPlacement8 = 0
    TeamPlacement9 = 0
    Team10Points = 0
    Team1Points = 0
    Team2Points = 0
    Team3Points = 0
    Team4Points = 0
    Team5Points = 0
    Team6Points = 0
    Team7Points = 0
    Team8Points = 0
    Team9Points = 0
    
    last_place = player_0
    third_last_place = player_000
    fourth_last_place = player_0000
    second_last_place = player_00
    first_place = player_100
    first_onTeam = player_1000
    end = []
    for people in teams:
        for players in people:
            count = count + 1
    count2 = 40
    while totalTeam > 1:
        index = 0
        while index < count2:
            for player in teams:
                for players in player:
                    players.random = random.randint(1,players.skill)
                    index = index + 1
        indexTeam = random.randint(0,totalTeam-1)
        for players in teams[indexTeam]:
            TeamTotal1 += 1
        TeamBattling1 = teams[indexTeam][0].team
        teamsCompeting.append(teams[indexTeam])
        teams.pop(indexTeam)

        totalTeam = totalTeam - 1
        indexTeam = random.randint(0,totalTeam-1)
        for players in teams[indexTeam]:
            TeamTotal2 += 1
        TeamBattling2 = teams[indexTeam][0].team
        teamsCompeting.append(teams[indexTeam])
        teams.pop(indexTeam)
        color1 = ''
        color2 = ''
        if TeamBattling1 == 1:
            color1 = 'RED'
        if TeamBattling1 == 2:
            color1 = 'YELLOW'
        if TeamBattling1 == 3:
            color1 = 'LIGHTYELLOW_EX'
        if TeamBattling1 == 4:
            color1 = 'LIGHTGREEN_EX'
        if TeamBattling1 == 5:
            color1 = "GREEN"
        if TeamBattling1 == 6:
            color1 = "CYAN"
        if TeamBattling1 == 7:
            color1 = "LIGHTCYAN_EX"
        if TeamBattling1 == 8:
            color1 = "BLUE"
        if TeamBattling1 == 9:
            color1 = "MAGENTA"
        if TeamBattling1 == 10:
            color1 = "LIGHTRED_EX"
        if TeamBattling2 == 1:
            color2 = 'RED'
        if TeamBattling2 == 2:
            color2 = 'YELLOW'
        if TeamBattling2 == 3:
            color2 = 'LIGHTYELLOW_EX'
        if TeamBattling2 == 4:
            color2 = 'LIGHTGREEN_EX'
        if TeamBattling2 == 5:
            color2 = "GREEN"
        if TeamBattling2 == 6:
            color2 = "CYAN"
        if TeamBattling2 == 7:
            color2 = "LIGHTCYAN_EX"
        if TeamBattling2 == 8:
            color2 = "BLUE"
        if TeamBattling2 == 9:
            color2 = "MAGENTA"
        if TeamBattling2 == 10:
            color2 = "LIGHTRED_EX"
        print(getattr(Fore,color1) + "Team "  + str(TeamBattling1) + Style.RESET_ALL + " vs." + getattr(Fore,color2) +  " Team " + str(TeamBattling2))
        print(getattr(Back,color1) + "                     " + getattr(Back,color2) + "                       ")
        for competing in teamsCompeting:
            for lister in competing:
                print(getattr(Fore, lister.color) + "Team " + str(lister.team) + " - " + str(lister.name))
        print(getattr(Back,color2) + "                     " + getattr(Back,color1) + "                       ")
        #normally 3
        time.sleep(timer*3)
        totalTeam = totalTeam - 1
        playersBattling = []
        for teamed in teamsCompeting:
            for players in teamed:
                playersBattling.append(players)
        if (TeamTotal1 >= TeamTotal2):
            Decider = TeamTotal2
        else:
            Decider = TeamTotal1
        counter = 0
        maximum = 0
        while counter < Decider:
            if (Decider == 4) or (Decider == 3 and TeamTotal1 == 3 and TeamTotal2 == 3) or (Decider == 2 and TeamTotal1 == 2 and TeamTotal2 == 2) or (Decider == 1 and TeamTotal1 == 1 and TeamTotal2 == 1):
                for players in playersBattling:
                    if players.random < minimum:
                        minimum = players.random
                        last_place.name = players.name
                        last_place.random = players.random
                        last_place.team = players.team
                        last_place.color = players.color
                    #new code
                for players in playersBattling:
                    if players.team != last_place.team:
                        if players.random > maximum:
                            maximum = players.random
                            first_place.name = players.name
                            first_place.name = players.name
                            first_place.random = players.random
                            first_place.team = players.team
                            first_place.color = players.color

                maximum = 0
                index3 = 0
                for player in playersBattling:
                    if player.name == last_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has died ☨")
                        end.append(playersBattling[index3])
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                index4 = 0
                for peopleS in teamsCompeting:
                    for people in peopleS:
                        if people.name == last_place.name:
                            peopleS.pop(index4)
                        index4 += 1
                    index4 = 0
                for people in teams:
                    for players in people:
                        players.coins = players.coins + 3
                for player in playersBattling:
                    player.coins = player.coins + 3
                index3=0
                for player in playersBattling:
                    if player.name == first_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has got a kill ☨")
                        killed.append(playersBattling[index3])
                        player.coins = player.coins + 70
                        player.kills = player.kills + 1
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                print(getattr(Fore,last_place.color) + str(last_place.name) +  Style.RESET_ALL + Style.BRIGHT + " was killed by " + Style.RESET_ALL + getattr(Fore,first_place.color) + str(first_place.name))
            if ((Decider == 3 and TeamTotal1 == 3 and TeamTotal2 == 4) or (Decider == 2 and TeamTotal1 == 2 and TeamTotal2 == 3) or (Decider == 3 and TeamTotal1 == 4 and TeamTotal2 == 3) or (Decider == 2 and TeamTotal1 == 3 and TeamTotal2 == 2) or (Decider == 1 and TeamTotal1 == 1 and TeamTotal2 == 2) or (Decider == 2 and TeamTotal1 == 3 and TeamTotal2 == 2) or (Decider == 1 and TeamTotal1 == 2 and TeamTotal2 == 1)):
                second_last_place = player_00
                for players in playersBattling:
                    if players.random < minimum:
                        minimum = players.random
                        last_place.name = players.name
                        last_place.random = players.random
                        last_place.team = players.team
                        last_place.color = players.color
                maximum = 0
                for players in playersBattling:
                    if players.team != last_place.team:
                        if players.random > maximum:
                            maximum = players.random
                            first_place.name = players.name
                            first_place.random = players.random
                            first_place.team = players.team
                            first_place.color = players.color
                maximum = 0
                index3 = 0
                for player in playersBattling:
                    if player.name == last_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has died ☨")
                        end.append(playersBattling[index3])
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                index4 = 0
                for peopleS in teamsCompeting:
                    for people in peopleS:
                        if people.name == last_place.name:
                            peopleS.pop(index4)
                        index4 += 1
                    index4 = 0
                for people in teams:
                    for players in people:
                        players.coins = players.coins + 3
                for player in playersBattling:
                    player.coins = player.coins + 3
                index3=0
                for player in playersBattling:
                    if player.name == first_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has got a kill ☨")
                        killed.append(playersBattling[index3])
                        player.coins = player.coins + 70
                        player.kills = player.kills + 1
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                print(getattr(Fore,last_place.color) + str(last_place.name) +  Style.RESET_ALL + Style.BRIGHT + " was killed by " + Style.RESET_ALL + getattr(Fore,first_place.color) + str(first_place.name))
                minimum = 100000
                for players in playersBattling:
                    if players.random < minimum:
                        minimum = players.random
                        second_last_place.name = players.name
                        second_last_place.random = players.random

            if ((Decider == 2 and TeamTotal1 == 2 and TeamTotal2 == 4) or (Decider == 2 and TeamTotal1 == 4 and TeamTotal2 == 2) or (Decider == 1 and TeamTotal1 == 3 and TeamTotal2 == 1) or (Decider == 1 and TeamTotal1 == 1 and TeamTotal2 == 3)):
                minimum = 0
                for players in playersBattling:
                    if (Decider == 1):
                        if (TeamTotal1 == 1):
                            if (players.team == TeamBattling1):
                                last_place.name = players.name
                                last_place.color = players.color
                                last_place.team = players.team
                        if (TeamTotal2 == 1):
                            if (players.team == TeamBattling2):
                                last_place.name = players.name
                                last_place.color = players.color
                                last_place.team = players.team
                        if (TeamTotal1 == 3):
                            if (players.team == TeamBattling1):
                                players.identifier = 1
                                if players.random > minimum:
                                    minimum = players.random
                                    first_place.name = players.name
                                    first_place.random = players.random
                                    first_place.color = players.color
                        if (TeamTotal2 == 3):
                            if (players.team == TeamBattling2):
                                players.identifier = 1
                                if players.random > minimum:
                                    minimum = players.random
                                    first_place.name = players.name
                                    first_place.random = players.random
                                    first_place.color = players.color
                
                    else:
                        minimum = 100000
                        if players.random < minimum:
                            third_last_place.name = second_last_place.name
                            second_last_place.name = last_place.name
                            minimum = players.random
                            last_place.name = players.name
                            last_place.random = players.random
                            last_place.team = players.team
                            last_place.color = players.color
                    maximum = 0
                    for players in playersBattling:
                        
                        if players.team != last_place.team:
                            if players.random > maximum:
                                maximum = players.random
                                first_place.name = players.name
                                first_place.random = players.random
                                first_place.team = players.team
                                first_place.color = players.color
                maximum = 0
                index3 = 0
                for player in playersBattling:
                    if player.name == last_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has died ☨")
                        end.append(playersBattling[index3])
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                
                index4 = 0
                for peopleS in teamsCompeting:
                    for people in peopleS:
                        if people.name == last_place.name:
                            peopleS.pop(index4)
                        index4 += 1
                    index4 = 0
                for people in teams:
                    for players in people:
                        players.coins = players.coins + 3
                for player in playersBattling:
                    player.coins = player.coins + 3
                index3=0
                for player in playersBattling:
                    if player.name == first_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has got a kill ☨")
                        killed.append(playersBattling[index3])
                        player.coins = player.coins + 70
                        player.kills = player.kills + 1
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                print(getattr(Fore,last_place.color) + str(last_place.name) +  Style.RESET_ALL + Style.BRIGHT + " was killed by " + Style.RESET_ALL + getattr(Fore,first_place.color) + str(first_place.name))
                minimum = 100000
                for players in playersBattling:
                    if players.random < minimum:
                        minimum = players.random
                        second_last_place.name = players.name
                        second_last_place.random = players.random
                minimum = 100000
                for players in playersBattling:
                    if players.random < minimum and players.random > second_last_place.random:
                        minimum = players.random
                        third_last_place.name = players.name
                        third_last_place.random = players.random
                for player in playersBattling:
                    if player.name == first_onTeam.name:
                        player.identifier = 0
            
            if ((Decider == 1 and TeamTotal1 == 1 and TeamTotal2 == 4) or (Decider == 1 and TeamTotal1 == 4 and TeamTotal2 == 1)):
                minimum = 0
                for players in playersBattling:
                    if (TeamTotal1 == 1):
                        if (players.team == TeamBattling1):
                            last_place.name = players.name
                            last_place.color = players.color
                    if (TeamTotal2 == 1):
                        if (players.team == TeamBattling2):
                            last_place.name = players.name
                            last_place.color = players.color
                    if (TeamTotal1 == 4):
                        if (players.team == TeamBattling1):
                            players.identifier = 1
                            if players.random > minimum:
                                minimum = players.random
                                first_place.name = players.name
                                first_place.random = players.random
                                first_place.color = players.color
                    if (TeamTotal2 == 4):
                        if (players.team == TeamBattling2):
                            players.identifier = 1
                            if players.random > minimum:
                                minimum = players.random
                                first_place.name = players.name
                                first_place.random = players.random
                                first_place.color = players.color
                        
                index3 = 0
                for player in playersBattling:
                    if player.name == last_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has died ☨")
                        end.append(playersBattling[index3])
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                for player in playersBattling:
                    if player.name == first_onTeam.name:
                        player.identifier = 0
                index4 = 0
                for peopleS in teamsCompeting:
                    for people in peopleS:
                        if people.name == last_place.name:
                            peopleS.pop(index4)
                        index4 += 1
                    index4 = 0
                for people in teams:
                    for players in people:
                        players.coins = players.coins + 3
                for player in playersBattling:
                    player.coins = player.coins + 3
                index3=0
                for player in playersBattling:
                    if player.name == first_place.name:
                        #print(getattr(Fore,player.color) + str(player.name) + " has got a kill ☨")
                        killed.append(playersBattling[index3])
                        player.coins = player.coins + 70
                        player.kills = player.kills + 1
                        playersBattling.pop(index3)
                    index3 = index3 + 1
                print(getattr(Fore,last_place.color) + str(last_place.name) +  Style.RESET_ALL + Style.BRIGHT + " was killed by " + Style.RESET_ALL + getattr(Fore,first_place.color) + str(first_place.name))
                minimum = 100000
                """for players in playersBattling:
                    if players.random < minimum:
                        minimum = players.random
                        second_last_place.name = players.name
                        second_last_place.random = players.random
                minimum = 100000
                for players in playersBattling:
                    if players.random < minimum and players.random > second_last_place.random:
                        minimum = players.random
                        third_last_place.name = players.name
                        third_last_place.random = players.random
                minimum = 100000
                for players in playersBattling:
                    if players.random < minimum and players.random > second_last_place.random and players.random > third_last_place.random:
                        minimum = players.random
                        fourth_last_place.name = players.name
                        fourth_last_place.random = players.random"""
            counter += 1
            minimum = 100000
        for players in playersBattling:
            if players.name == second_last_place.name:
                players.identifier = 1
            if players.name == third_last_place.name:
                players.identifier = 1
            if players.name == fourth_last_place.name:
                players.identifier = 1
            players.identifier = 0
        second_last_place.name = "null"
        third_last_place.name = "null"
        fourth_last_place.name = "null"
        first_onTeam.name = "null"
        playersBattling.extend(killed)
        killed = []
        if (TeamBattling2 == 1 or TeamBattling1 == 1):
            leftOn1 = 0
            for remaining in playersBattling:
                if remaining.team == 1:
                    leftOn1 += 1
            if leftOn1 == 0:
                TeamPlacement1 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 1 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 2 or TeamBattling1 == 2):
            leftOn2 = 0
            for remaining in playersBattling:
                if remaining.team == 2:
                    leftOn2 += 1
            if leftOn2 == 0:
                TeamPlacement2 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 2 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 3 or TeamBattling1 == 3):
            leftOn3 = 0
            for remaining in playersBattling:
                if remaining.team == 3:
                    leftOn3 += 1
            if leftOn3 == 0:
                TeamPlacement3 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 3 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 4 or TeamBattling1 == 4):
            leftOn4 = 0
            for remaining in playersBattling:
                if remaining.team == 4:
                    leftOn4 += 1
            if leftOn4 == 0:
                TeamPlacement4 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 4 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 5 or TeamBattling1 == 5):
            leftOn5 = 0
            for remaining in playersBattling:
                if remaining.team == 5:
                    leftOn5 += 1
            if leftOn5 == 0:
                TeamPlacement5 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 5 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 6 or TeamBattling1 == 6):
            leftOn6 = 0
            for remaining in playersBattling:
                if remaining.team == 6:
                    leftOn6 += 1
            if leftOn6 == 0:
                TeamPlacement6 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 6 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 7 or TeamBattling1 == 7):
            leftOn7 = 0
            for remaining in playersBattling:
                if remaining.team == 7:
                    leftOn7 += 1
            if leftOn7 == 0:
                TeamPlacement7 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 7 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 8 or TeamBattling1 == 8):
            leftOn8 = 0
            for remaining in playersBattling:
                if remaining.team == 8:
                    leftOn8 += 1
            if leftOn8 == 0:
                TeamPlacement8 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 8 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 9 or TeamBattling1 == 9):
            leftOn9 = 0
            for remaining in playersBattling:
                if remaining.team == 9:
                    leftOn9 += 1
            if leftOn9 == 0:
                TeamPlacement9 = TeamPlacement
                TeamPlacement = TeamPlacement + 1 
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 9 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        if (TeamBattling2 == 10 or TeamBattling1 == 10):
            leftOn10 = 0
            for remaining in playersBattling:
                if remaining.team == 10:
                    leftOn10 += 1
            if leftOn10 == 0:
                TeamPlacement10 = TeamPlacement
                TeamPlacement = TeamPlacement + 1
                print(Back.BLACK + "                                            ")
                print(Back.BLACK + "         TEAM 10 HAS BEEN ELIMINATED         ")
                print(Back.BLACK + "                                            ")
            else:
                totalTeam += 1
        teamsLength = 0
        for teames in teamsCompeting:
            teamsLength += 1
        whileCount = 0
        while (whileCount < teamsLength):
            if (teamsCompeting[teamsLength-1] != []):
                teams.append(teamsCompeting[teamsLength-1])
                teamsCompeting.pop(teamsLength-1)
            teamsLength = teamsLength - 1 
        TeamTotal1 = 0
        TeamTotal2 = 0
        print("")
        print(Style.BRIGHT + Back.BLACK + "                          ✧  Remaining ✧                         ")
        print("")
        for people in teams:
            for actual in people:
                print(getattr(Fore,actual.color) + "Team " + str(actual.team) + " - " + str(actual.name))
        print("")
        #normally 3
        time.sleep(timer*3)
    winningNumber = 0
    totalWinners = 0
    for peopleReamining in teams:
        for winners in peopleReamining:
            totalWinners += 1
            winningNumber = winners.team
    for people in end:
        if people.team == winningNumber:
            people.coins += 80
    for persons in teams:
        for peopled in persons:
            peopled.coins = peopled.coins + 80
            end.append(peopled)
        teams.pop(0)

    if (TeamPlacement1 == 0):
        Team1Points = 82
    if (TeamPlacement1 == 1):
        Team1Points = 92
    if (TeamPlacement1 == 2):
        Team1Points = 102
    if (TeamPlacement1 == 3):
        Team1Points = 112
    if (TeamPlacement1 == 4):
        Team1Points = 122
    if (TeamPlacement1 == 5):
        Team1Points = 132
    if (TeamPlacement1 == 6):
        Team1Points = 142
    if (TeamPlacement1 == 7):
        Team1Points = 152
    if (TeamPlacement1 == 8):
        Team1Points = 162
    if (TeamPlacement1 == 9):
        Team1Points = 175
    if (TeamPlacement2 == 0):
        Team2Points = 82
    if (TeamPlacement2 == 1):
        Team2Points = 92
    if (TeamPlacement2 == 2):
        Team2Points = 102
    if (TeamPlacement2 == 3):
        Team2Points = 112
    if (TeamPlacement2 == 4):
        Team2Points = 122
    if (TeamPlacement2 == 5):
        Team2Points = 132
    if (TeamPlacement2 == 6):
        Team2Points = 142
    if (TeamPlacement2 == 7):
        Team2Points = 152
    if (TeamPlacement2 == 8):
        Team2Points = 162
    if (TeamPlacement2 == 9):
        Team2Points = 175
    if (TeamPlacement3 == 0):
        Team3Points = 82
    if (TeamPlacement3 == 1):
        Team3Points = 92
    if (TeamPlacement3 == 2):
        Team3Points = 102
    if (TeamPlacement3 == 3):
        Team3Points = 112
    if (TeamPlacement3 == 4):
        Team3Points = 122
    if (TeamPlacement3 == 5):
        Team3Points = 132
    if (TeamPlacement3 == 6):
        Team3Points = 142
    if (TeamPlacement3 == 7):
        Team3Points = 152
    if (TeamPlacement3 == 8):
        Team3Points = 162
    if (TeamPlacement4 == 9):
        Team3Points = 175
    if (TeamPlacement4 == 0):
        Team4Points = 82
    if (TeamPlacement4 == 1):
        Team4Points = 92
    if (TeamPlacement4 == 2):
        Team4Points = 102
    if (TeamPlacement4 == 3):
        Team4Points = 112
    if (TeamPlacement4 == 4):
        Team4Points = 122
    if (TeamPlacement4 == 5):
        Team4Points = 132
    if (TeamPlacement4 == 6):
        Team4Points = 142
    if (TeamPlacement4 == 7):
        Team4Points = 152
    if (TeamPlacement4 == 8):
        Team4Points = 162
    if (TeamPlacement4 == 9):
        Team4Points = 175
    if (TeamPlacement5 == 0):
        Team5Points = 82
    if (TeamPlacement5 == 1):
        Team5Points = 92
    if (TeamPlacement5 == 2):
        Team5Points = 102
    if (TeamPlacement5 == 3):
        Team5Points = 112
    if (TeamPlacement5 == 4):
        Team5Points = 122
    if (TeamPlacement5 == 5):
        Team5Points = 132
    if (TeamPlacement5 == 6):
        Team5Points = 142
    if (TeamPlacement5 == 7):
        Team5Points = 152
    if (TeamPlacement5 == 8):
        Team5Points = 162
    if (TeamPlacement5 == 9):
        Team5Points = 175
    if (TeamPlacement6 == 0):
        Team6Points = 82
    if (TeamPlacement6 == 1):
        Team6Points = 92
    if (TeamPlacement6 == 2):
        Team6Points = 102
    if (TeamPlacement6 == 3):
        Team6Points = 112
    if (TeamPlacement6 == 4):
        Team6Points = 122
    if (TeamPlacement6 == 5):
        Team6Points = 132
    if (TeamPlacement6 == 6):
        Team6Points = 142
    if (TeamPlacement6 == 7):
        Team6Points = 152
    if (TeamPlacement6 == 8):
        Team6Points = 162
    if (TeamPlacement6 == 9):
        Team6Points = 175
    if (TeamPlacement7 == 0):
        Team7Points = 82
    if (TeamPlacement7 == 1):
        Team7Points = 92
    if (TeamPlacement7 == 2):
        Team7Points = 102
    if (TeamPlacement7 == 3):
        Team7Points = 112
    if (TeamPlacement7 == 4):
        Team7Points = 122
    if (TeamPlacement7 == 5):
        Team7Points = 132
    if (TeamPlacement7 == 6):
        Team7Points = 142
    if (TeamPlacement7 == 7):
        Team7Points = 152
    if (TeamPlacement7 == 8):
        Team7Points = 162
    if (TeamPlacement7 == 9):
        Team7Points = 175
    if (TeamPlacement8 == 0):
        Team8Points = 82
    if (TeamPlacement8 == 1):
        Team8Points = 92
    if (TeamPlacement8 == 2):
        Team8Points = 102
    if (TeamPlacement8 == 3):
        Team8Points = 112
    if (TeamPlacement8 == 4):
        Team8Points = 122
    if (TeamPlacement8 == 5):
        Team8Points = 132
    if (TeamPlacement8 == 6):
        Team8Points = 142
    if (TeamPlacement8 == 7):
        Team8Points = 152
    if (TeamPlacement8 == 8):
        Team8Points = 162
    if (TeamPlacement8 == 9):
        Team8Points = 175
    if (TeamPlacement9 == 0):
        Team9Points = 82
    if (TeamPlacement9 == 1):
        Team9Points = 92
    if (TeamPlacement9 == 2):
        Team9Points = 102
    if (TeamPlacement9 == 3):
        Team9Points = 112
    if (TeamPlacement9 == 4):
        Team9Points = 122
    if (TeamPlacement9 == 5):
        Team9Points = 132
    if (TeamPlacement9 == 6):
        Team9Points = 142
    if (TeamPlacement9 == 7):
        Team9Points = 152
    if (TeamPlacement9 == 8):
        Team9Points = 162
    if (TeamPlacement9 == 9):
        Team9Points = 175
    if (TeamPlacement10 == 0):
        Team10Points = 82
    if (TeamPlacement10 == 1):
        Team10Points = 92
    if (TeamPlacement10 == 2):
        Team10Points = 102
    if (TeamPlacement10 == 3):
        Team10Points = 112
    if (TeamPlacement10 == 4):
        Team10Points = 122
    if (TeamPlacement10 == 5):
        Team10Points = 132
    if (TeamPlacement10 == 6):
        Team10Points = 142
    if (TeamPlacement10 == 7):
        Team10Points = 152
    if (TeamPlacement10 == 8):
        Team10Points = 162
    if (TeamPlacement10 == 9):
        Team10Points = 175

    

    for player in end:
        if player.team == 1:
            player.coins = player.coins + Team1Points
        if player.team == 2:
            player.coins = player.coins + Team2Points
        if player.team == 3:
            player.coins = player.coins + Team3Points
        if player.team == 4:
            player.coins = player.coins + Team4Points
        if player.team == 5:
            player.coins = player.coins + Team5Points
        if player.team == 6:
            player.coins = player.coins + Team6Points
        if player.team == 7:
            player.coins = player.coins + Team7Points
        if player.team == 8:
            player.coins = player.coins + Team8Points
        if player.team == 9:
            player.coins = player.coins + Team9Points
        if player.team == 10:
            player.coins = player.coins + Team10Points
    sorted = []
    for player in end:
        print(player.name + " has " + str(player.coins) + " total coins" + " and " + str(player.kills) + " total kills")
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    totalKills = 0
    for players in end:
        totalKills = totalKills + players.kills
    print(totalKills)
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    for players in final:
        print(players.coins)
    for players in final:
        print(players.name)

        





    return final
    


def HITW(players,round):
    
    player_0 = Player("null",0,0,0,0,0,0,0,"team1")
    count = 0
    index = 0
    index2 = 0
    Placement = 40
    count2 = 0
    minimum = 100000
    last_place = player_0
    end = []
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    for player in players:
        count = count + 1
    count2 = count
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill) + random.randint(1,players[index].skill)
            index = index + 1
        if count2 == 3:
            for player in players:
                player.coins = player.coins + 34
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(Placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+34🪙 ]   " + "\n")
            Placement -= 1
        elif count2 == 2:
            for player in players:
                player.coins = player.coins + 44
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(Placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has been eliminated. [+44🪙 ]   " + "\n")
            Placement -= 1
        elif count2 == 1:
            for player in players:
                player.coins = player.coins + 34
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(Placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL+ " has won the round! [+34🪙 ]   " + "\n")
            Placement -= 1
        elif count2 == 40:
            for player in players:
                player.coins = player.coins + 0
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(Placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL  + " has been eliminated. [+4🪙 ]   " + "\n")
            Placement -= 1
        else:
            for player in players:
                player.coins = player.coins + 4
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print( "『 " + str(Placement) +" 』 " + getattr(Fore, last_place.color) + last_place.name + Style.RESET_ALL + " has been eliminated. [+4🪙 ]   " + "\n")
            Placement -= 1
        index3 = 0
        #normally 0.5
        time.sleep(timer*0.5)
        for player in players:
            if player.name == last_place.name:
                end.append(players[index3])
                players.pop(index3)
            index3 = index3 + 1
            
        minimum = 10000
        index3 = 0
        index = 0
        index2 = index2 + 1
        count2 = count2 - 1
    sorted = []
    roundsummary = ''

    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 2:
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
    if round == 3:
        for players in final:
            roundsummary += str(players.coins) + "\n"
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")
    return final,roundsummary
    

def Disco(players,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    Placement = 40
    count2 = 0
    minimum = 100000
    round4 = 1
    lefton1 = 0
    lefton2 = 0
    lefton3 = 0
    lefton4 = 0
    lefton5 = 0
    lefton6 = 0
    lefton7 = 0
    lefton8 = 0
    lefton9 = 0
    lefton10 = 0
    Placement = 40
    last_place = player_0
    end = []
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    for player in players:
        count = count + 1
    count2 = count
    while round4 < 61:
        count2 = 0
        for player in players:
            count2 = count2 + 1
        index = 0
        while index < count2:
            players[index].random = random.randint(1,players[index].skill) + random.randint(1,players[index].skill)
            index = index + 1
        print(Back.WHITE + Style.BRIGHT +  "✯ -" + Back.GREEN + "=" + Back.CYAN + "-" + Back.MAGENTA + "=" + Back.YELLOW + "-" + Back.RED + "=" + Back.LIGHTGREEN_EX + "-" + Back.LIGHTBLACK_EX + " " 
        + Back.BLUE + Style.DIM + " ⋆⭒⋆ " + Back.LIGHTCYAN_EX + " Round "  + str(round4) + " [+2🪙 ]" + Back.BLUE + " ⋆⭒⋆ " + Back.LIGHTBLACK_EX + " " + Back.LIGHTGREEN_EX + "-" + Back.RED + "=" + Back.YELLOW + "-" + Back.MAGENTA + 
        "=" + Back.CYAN + "-" + Back.GREEN + "=" + Back.WHITE + "- ✯ ")
        index3 = 0
        if round4 < 10:
            for player in players:
                if player.random < 5:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. ")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        if round4 < 20 and round4 >= 10:
            for player in players:
                if player.random < 10:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. ")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        if round4 < 30 and round4 >= 20:
            for player in players:
                if player.random < 18:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. ")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        if round4 < 40 and round4 >= 30:
            for player in players:
                if player.random < 24:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. ")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        if round4 < 50 and round4 >= 40:
            for player in players:
                if player.random < 30:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. ")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        if round4 < 60 and round4 >= 50:
            for player in players:
                if player.random < 40:
                    player.kills = round4-1
                    print( "『 " + str(Placement) +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has been eliminated. " + "\n")
                    Placement -= 1
                    end.append(players[index3])
                    players.pop(index3)

                index3 += 1
        lefton1 = 0
        lefton2 = 0
        lefton3 = 0
        lefton4 = 0
        lefton5 = 0
        lefton6 = 0
        lefton7 = 0
        lefton8 = 0
        lefton9 = 0
        lefton10 = 0
        for player in players:
            if player.team == 1:
                lefton1 += 1
            if player.team == 2:
                lefton2 += 1
            if player.team == 3:
                lefton3 += 1
            if player.team == 4:
                lefton4 += 1
            if player.team == 5:
                lefton5 += 1
            if player.team == 6:
                lefton6 += 1
            if player.team == 7:
                lefton7 += 1
            if player.team == 8:
                lefton8 += 1
            if player.team == 9:
                lefton9 += 1
            if player.team == 10:
                lefton10 += 1
        if round4 == 10:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                       ✧  10 Rounds Survived [+10🪙 ] ✧                    ")
            print("")
            for player in players:
                player.coins += 12
        if round4 == 20:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                       ✧  20 Rounds Survived [+10🪙 ] ✧                    ")
            print("")
            for player in players:
                player.coins += 12
        if round4 == 30:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                       ✧  30 Rounds Survived [+10🪙 ] ✧                    ")
            print(Style.BRIGHT + Back.BLACK + "                          ✧  Remaining on Teams ✧                         ")
            print(Fore.RED + "1" + Style.RESET_ALL + "       " + Fore.YELLOW + "2" + Style.RESET_ALL + "       " + Fore.LIGHTYELLOW_EX + "3" + Style.RESET_ALL + "       " + 
            Fore.LIGHTGREEN_EX + "4" + Style.RESET_ALL + "       " + Fore.BLUE + "5" + Style.RESET_ALL + "       " + Fore.LIGHTCYAN_EX + "6" + Style.RESET_ALL + "       " + Fore.CYAN + "7" + Style.RESET_ALL + "       " +
            Fore.MAGENTA + "8" + Style.RESET_ALL + "       " + Fore.LIGHTRED_EX + "9" + Style.RESET_ALL + "      " + Fore.GREEN + "10" + Style.RESET_ALL + "       " )
            print(Style.BRIGHT + str(lefton1) + "       " + str(lefton2) + "       " +str(lefton3) + "       " +str(lefton4) + "       " +str(lefton5) + "       " +str(lefton6) + "       " +str(lefton7) + "       " +str(lefton8) + "       " +str(lefton9) + "       " +str(lefton10) + "\n")
            time.sleep(timer*5)
            for player in players:
                player.coins += 12
        if round4 == 40:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                       ✧  40 Rounds Survived [+10🪙 ] ✧                    ")
            print(Style.BRIGHT + Back.BLACK + "                          ✧  Remaining on Teams ✧                         ")
            print(Fore.RED + "1" + Style.RESET_ALL + "       " + Fore.YELLOW + "2" + Style.RESET_ALL + "       " + Fore.LIGHTYELLOW_EX + "3" + Style.RESET_ALL + "       " + 
            Fore.LIGHTGREEN_EX + "4" + Style.RESET_ALL + "       " + Fore.BLUE + "5" + Style.RESET_ALL + "       " + Fore.LIGHTCYAN_EX + "6" + Style.RESET_ALL + "       " + Fore.CYAN + "7" + Style.RESET_ALL + "       " +
            Fore.MAGENTA + "8" + Style.RESET_ALL + "       " + Fore.LIGHTRED_EX + "9" + Style.RESET_ALL + "      " + Fore.GREEN + "10" + Style.RESET_ALL + "       " )
            print(Style.BRIGHT + str(lefton1) + "       " + str(lefton2) + "       " +str(lefton3) + "       " +str(lefton4) + "       " +str(lefton5) + "       " +str(lefton6) + "       " +str(lefton7) + "       " +str(lefton8) + "       " +str(lefton9) + "       " +str(lefton10) + "\n")
            time.sleep(timer*5)
            for player in players:
                player.coins += 12
        if round4 == 50:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                       ✧  50 Rounds Survived [+10🪙 ] ✧                    ")
            print(Style.BRIGHT + Back.BLACK + "                          ✧  Remaining on Teams ✧                         ")
            print(Fore.RED + "1" + Style.RESET_ALL + "       " + Fore.YELLOW + "2" + Style.RESET_ALL + "       " + Fore.LIGHTYELLOW_EX + "3" + Style.RESET_ALL + "       " + 
            Fore.LIGHTGREEN_EX + "4" + Style.RESET_ALL + "       " + Fore.BLUE + "5" + Style.RESET_ALL + "       " + Fore.LIGHTCYAN_EX + "6" + Style.RESET_ALL + "       " + Fore.CYAN + "7" + Style.RESET_ALL + "       " +
            Fore.MAGENTA + "8" + Style.RESET_ALL + "       " + Fore.LIGHTRED_EX + "9" + Style.RESET_ALL + "      " + Fore.GREEN + "10" + Style.RESET_ALL + "       " )
            print(Style.BRIGHT + str(lefton1) + "       " + str(lefton2) + "       " +str(lefton3) + "       " +str(lefton4) + "       " +str(lefton5) + "       " +str(lefton6) + "       " +str(lefton7) + "       " +str(lefton8) + "       " +str(lefton9) + "       " +str(lefton10) + "\n")
            time.sleep(timer*5)
            for player in players:
                player.coins += 12
        index3 = 0
        if round4 == 60:
            print("")
            print(Style.BRIGHT + Back.BLACK + "                           ✧  Survived [+52🪙 ] ✧                    ")
            if len(players) == 0:
                print("")
                print(Style.BRIGHT + Back.BLACK + "                             ✧  No One Survived ✧                     ")
            else:
                for player in players:
                    player.kills = round4
                    player.coins += 52
                    print( "『 " + "1" +" 』 " + getattr(Fore, player.color) + player.name + Style.RESET_ALL + " has survived to the end. " + "\n")
                
                end.extend(players)
                players = []
        round4 += 1
        for player in players:
            player.coins += 2
        index3 = 0
        index = 0
        index2 = index2 + 1
        count2 = count2 - 1
        time.sleep(timer*1)
    sorted = []
    for player in end:
        print(player.name + " survived " + str(player.kills) + " total rounds" )
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    roundsummary = ''
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    for players in final:
        print(players.kills)
    for players in final:
        print(players.name)
    for players in final:
        print(players.coins)
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
        for players in final:
            roundsummary += players.name + "\n"
        for players in final:
            roundsummary += str(players.kills) + "\n"
    if round == 2:
        for players in final:
            roundsummary += players.name + "\n"
        for players in final:
            roundsummary += str(players.kills) + "\n"
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
    if round == 3:
        for players in final:
            roundsummary += str(players.coins) + "\n"
        
        for players in final:
            roundsummary += players.name + "\n"
        for players in final:
            roundsummary += str(players.kills) + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")

        





    return final,roundsummary

def GR(players, players2):
    room_number = 1
    player_0 = Team(0,0,0,0,0,"RED")
    count = 0
    index = 0
    new_list = []
    new_list = players
    index2 = 0
    index3 = 0
    count2 = 10
    minimum = 100000
    last_place = player_0
    end = []
    while index2 < 8:
        index3 = 0
        count2 = 10
        if (index2 != 0):
            players = end
            end = []
        while index3 < 10:
            minimum = 100000

            while index < count2:
                players[index].random = random.randint(1,players[index].skill)
                index = index + 1
            for player in players:
                player.coins = player.coins + 17
                if player.random < minimum:
                    minimum = player.random
                    last_place.number = player.number

            index4 = 0
            for player in players:
                if player.number == last_place.number:
                    end.append(player)
                    players.pop(index4)
                index4 = index4 + 1
            index3 = index3 +1
            count2 = count2 - 1
            index = 0
        index2 = index2 + 1
        index8 = 0

        print(Style.BRIGHT + Back.BLACK + "                      ✧  Room " +  str(room_number) + " ✧                     ")
        room_number = room_number + 1   
        for players in end:
            if (index8 == 0):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+17🪙 ]")
            if (index8 == 1):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+34🪙 ]")
            if (index8 == 2):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+51🪙 ]")
            if (index8 == 3):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+68🪙 ]")
            if (index8 == 4):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+85🪙 ]")
            if (index8 == 5):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+102🪙 ]")
            if (index8 == 6):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+119🪙 ]")
            if (index8 == 7):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+136🪙 ]")
            if (index8 == 8):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+153🪙 ]")
            if (index8 == 9):
                print(getattr(Fore, players.color) + "Team " + str(players.number) + " Have " + str(players.coins) + " Coins" + "[+170🪙 ]")
            index8 = index8 + 1
            
        

        #normally 20    
        time.sleep(timer*10)
    final = []
    index6 = 0
    index5 = 0
    popindex = 0
    while index6 < 10:
        maximum = 100000
        most = player_0
        for players in end:
            coins = players.coins
            if coins < maximum:
                maximum = coins
                most = players
                popindex = index5
            index5 = index5 + 1
        if end:
            end.pop(popindex)
            final.append(most)
        index6 = index6 + 1
        index5 = 0
    index7 = 0
    for teams in final:
        if index7 == 0:
            teams.coins = teams.coins + 55
        if index7 == 1:
            teams.coins = teams.coins + 75
        if index7 == 2:
            teams.coins = teams.coins + 95
        if index7 == 3:
            teams.coins = teams.coins + 120
        if index7 == 4:
            teams.coins = teams.coins + 155
        if index7 == 5:
            teams.coins = teams.coins + 200
        if index7 == 6:
            teams.coins = teams.coins + 255
        if index7 == 7:
            teams.coins = teams.coins + 320
        if index7 == 8:
            teams.coins = teams.coins + 400
        if index7 == 9:
            teams.coins = teams.coins + 500
        index7 = index7 + 1
    for team in final:
        if (team.number == 1):
            team1 = team
        if (team.number == 2):
            team2 = team
        if (team.number == 3):
            team3 = team
        if (team.number == 4):
            team4 = team
        if (team.number == 5):
            team5 = team
        if (team.number == 6):
            team6 = team
        if (team.number == 7):
            team7 = team
        if (team.number == 8):
            team8 = team
        if (team.number == 9):
            team9 = team
        if (team.number == 10):
            team10 = team

    for player in players2:
        if (player.team == 1):
            player.coins = math.trunc(team1.coins / 4)
        if (player.team == 2):
            player.coins = math.trunc(team2.coins / 4)
        if (player.team == 3):
            player.coins = math.trunc(team3.coins / 4)
        if (player.team == 4):
            player.coins = math.trunc(team4.coins / 4)
        if (player.team == 5):
            player.coins = math.trunc(team5.coins / 4)
        if (player.team == 6):
            player.coins = math.trunc(team6.coins / 4)
        if (player.team == 7):
            player.coins = math.trunc(team7.coins / 4)
        if (player.team == 8):
            player.coins = math.trunc(team8.coins / 4)
        if (player.team == 9):
            player.coins = math.trunc(team9.coins / 4)
        if (player.team == 10):
            player.coins = math.trunc(team10.coins / 4)

            

                
    

    print("---------------FINAL SCORES-------------")
    for players in final:
        print("Team " + str(players.number) + " Scored " + str(players.coins) + " Coins")
    print("---------------STATISTICS---------------")
    for players in final:
        print(players.coins)
    for players in final:
        print(players.number)
    for players in players2:
        print(players.coins)
    for players in players2:
        print(players.name)
    return players2



def GR_Team_Total(total,multiplier):
    @dataclass 
    class finalTeam:
        coins: int
        name: str
        color: str
    team_1 = finalTeam(0,"Team 1","RED")
    team_2 = finalTeam(0,"Team 2","YELLOW")
    team_3 = finalTeam(0,"Team 3","LIGHTYELLOW_EX")
    team_4 = finalTeam(0,"Team 4","LIGHTGREEN_EX")
    team_5 = finalTeam(0,"Team 5","GREEN")
    team_6 = finalTeam(0,"Team 6","CYAN")
    team_7 = finalTeam(0,"Team 7","LIGHTCYAN_EX")
    team_8 = finalTeam(0,"Team 8","BLUE")
    team_9 = finalTeam(0,"Team 9","MAGENTA")
    team_10 = finalTeam(0,"Team 10","LIGHTRED_EX")
    for parts in total:
        if parts.number == 1:
            team_1.coins = team_1.coins + parts.coins
        if parts.number == 2:
            team_2.coins = team_2.coins + parts.coins
        if parts.number == 3:
            team_3.coins = team_3.coins + parts.coins
        if parts.number == 4:
            team_4.coins = team_4.coins + parts.coins
        if parts.number == 5:
            team_5.coins = team_5.coins + parts.coins
        if parts.number == 6:
            team_6.coins = team_6.coins + parts.coins
        if parts.number == 7:
            team_7.coins = team_7.coins + parts.coins
        if parts.number == 8:
            team_8.coins = team_8.coins + parts.coins
        if parts.number == 9:
            team_9.coins = team_9.coins + parts.coins
        if parts.number == 10:
            team_10.coins = team_10.coins + parts.coins
    team_1.coins = team_1.coins * multiplier
    team_2.coins = team_2.coins * multiplier
    team_3.coins = team_3.coins * multiplier
    team_4.coins = team_4.coins * multiplier
    team_5.coins = team_5.coins * multiplier
    team_6.coins = team_6.coins * multiplier
    team_7.coins = team_7.coins * multiplier
    team_8.coins = team_8.coins * multiplier
    team_9.coins = team_9.coins * multiplier
    team_10.coins = team_10.coins * multiplier
    sort_list = [team_1,team_10,team_2,team_3,team_4,team_5,team_6,team_7,team_8,team_9]
    sorted_list = sorted(sort_list, key=operator.attrgetter('coins'))
    sorted_list.reverse()
    for teamed in sorted_list:
        print(getattr(Back, teamed.color)  + teamed.name + Style.RESET_ALL + " Points: " + Style.BRIGHT + Back.BLACK + str(math.trunc(teamed.coins)))
    for teamed in sort_list:
        print(math.trunc(teamed.coins))
    sorted_y = sorted(total, key=operator.attrgetter('coins'))
    sorted_y.reverse()
    counted = 1


def SB(players,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    player_100 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    Placement = 40
    minimum = 100000
    last_place = player_0
    first_place = player_100
    end = []
    for player in players:
        count = count + 1
    count2 = 40
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        if count2 == 40:
            counting = 0
            while (counting < 1):
                for player in players:
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 39
            index2 = 1
        if count2 == 39:
            counting = 0
            while (counting < 19):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                player.coins = player.coins + 35
                player.kills = player.kills + 1
            index2 = 1
            
        if count2 == 20:
            counting = 0
            while (counting < 10):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                player.coins = player.coins + 35
                player.kills = player.kills + 1
            index2 = 1
        if count2 == 10:
            counting = 0
            while (counting < 5):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                player.coins = player.coins + 35
                player.kills = player.kills + 1
            index2 = 1
        if count2 == 5:
            maximum = 0
            counting = 0
            while (counting < 2):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random

                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
            for player in players:
                    if player.name != last_place.name:
                        player.coins = player.coins + 35
                        player.kills = player.kills + 1
            index2 = 1
            
        if count2 == 3:
            maximum = 0
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random

                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
            for player in players:
                    if player.name != last_place.name:
                        player.coins = player.coins + 35
                        player.kills = player.kills + 1
            index2 = 1
        if count2 == 2:
            maximum = 0
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 3
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random

                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            for player in players:
                    player.coins = player.coins + 73
                    player.kills = player.kills + 1
                    end.append(players[0])
                    players.pop(0)
            index2 = 50
            
        minimum = 10000
        index = 0
        count = 20
        if count2 == 3:
            count2 = 2
        if count2 == 5:
            count2 = 3
        if count2 == 10:
            count2 = 5
        if count2 == 20:
            count2 = 10
        if count2 == 39:
            count2 = 20

    sorted = []
    counter = 0
    for player in end:
        if (counter == 20):
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Top 20 ✧                     ")
            print("")
            #normally 4
            time.sleep(timer*4)
        if (counter == 30):
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Top 10 ✧                     ")
            print("")
            #normally 4
            time.sleep(timer*4)
        if (counter == 35):
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Top 5 ✧                     ")
            print("")
            #normally 4
            time.sleep(timer*4)
        if (counter == 37):
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Top 3 ✧                     ")
            print("")
            #normally 4
            time.sleep(timer*4)
        if (counter == 38):
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Top 2 ✧                     ")
            print("")
            #normally 4
            time.sleep(timer*4)
        print("『 " + str(Placement) +" 』 " + getattr(Fore, player.color) +  player.name + Style.RESET_ALL + " [" + str(player.coins) + "🪙 ]  [" + str(player.kills) + "⚔︎ ]" + "\n")
        Placement -= 1
        counter = counter + 1
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    roundsummary = ''
    '''for players in final:
        print(players.coins)
    for players in final:
        print(players.name)'''
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 2:
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
    if round == 3:
        for players in final:
            roundsummary += str(players.coins) + "\n"
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")

        





    return final,roundsummary
    


def TGTTOS(players,teams,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    team1left = 4
    team2left = 4
    team3left = 4
    team4left = 4
    team5left = 4
    team6left = 4
    team7left = 4
    team8left = 4
    team9left = 4
    team10left = 4
    timesdone = 0
    minimum = 100000
    last_place = player_0
    end = []
    end2 = []
    teamsin = []
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    placement = 40
    for player in players:
        count = count + 1
    count2 = count
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        if count2 == 10:
            for player in players:
                player.coins = player.coins + 36
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has finished. [+63🪙 ]   " + "\n")
            placement -= 1
        elif count2 < 10:
            for player in players:
                player.coins = player.coins + 6
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has finished. [+9🪙 ]   " + "\n")
            placement -= 1
        else:
            for player in players:
                player.coins = player.coins + 1
                if player.random < minimum:
                    minimum = player.random
                    last_place.name = player.name
                    last_place.random = player.random
                    last_place.team = player.team
                    last_place.color = player.color
            print("『 " + str(placement) +" 』 " + getattr(Fore, last_place.color) +  last_place.name + Style.RESET_ALL + " has finished. [+1🪙 ]   " + "\n")
            placement -= 1
        index3 = 0
        for player in players:
            if player.name == last_place.name:
                if player.team == 1:
                    team1left = team1left -1
                if player.team == 2:
                    team2left = team2left -1
                if player.team == 3:
                    team3left = team3left -1
                if player.team == 4:
                    team4left = team4left -1
                if player.team == 5:
                    team5left = team5left -1
                if player.team == 6:
                    team6left = team6left -1
                if player.team == 7:
                    team7left = team7left -1
                if player.team == 8:
                    team8left = team8left -1
                if player.team == 9:
                    team9left = team9left -1
                if player.team == 10:
                    team10left = team10left -1
                end.append(players[index3])
                players.pop(index3)
            index3 = index3 + 1
        teamnumber = 0
        if team1left == 3:
            index7 = 0
            for team in teams:
                if team.number == 1:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team1left = 50
        if team2left == 3:
            index7 = 0
            for team in teams:
                if team.number == 2:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team2left = 50
        if team3left == 3:
            index7 = 0
            for team in teams:
                if team.number == 3:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team3left = 50
        if team4left == 3:
            index7 = 0
            for team in teams:
                if team.number == 4:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team4left = 50
        if team5left == 3:
            index7 = 0
            for team in teams:
                if team.number == 5:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team5left = 50
        if team6left == 3:
            index7 = 0
            for team in teams:
                if team.number == 6:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team6left = 50
        if team7left == 3:
            index7 = 0
            for team in teams:
                if team.number == 7:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team7left = 50
        if team8left == 3:
            index7 = 0
            for team in teams:
                if team.number == 8:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team8left = 50
        if team9left == 3:
            index7 = 0
            for team in teams:
                if team.number == 9:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team9left = 50
        if team10left == 3:
            index7 = 0
            for team in teams:
                if team.number == 10:
                    teamnumber = index7
                    end2.append(teams[teamnumber])
                    teams.pop(teamnumber)
                index7 = index7 + 1
            team10left = 50
        countteams = 0
        
        for team in teams:
            countteams = countteams + 1
        if (countteams == 4 and timesdone == 0):
            for team in teams:
                teamsin.append(team.number)
                if (team.number == 1):
                    for player in players:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                if (team.number == 2):
                    for player in players:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                if (team.number == 3):
                    for player in players:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                if (team.number == 4):
                    for player in players:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                if (team.number == 5):
                    for player in players:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                if (team.number == 6):
                    for player in players:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                if (team.number == 7):
                    for player in players:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                if (team.number == 8):
                    for player in players:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                if (team.number == 9):
                    for player in players:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                if (team.number == 10):
                    for player in players:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                
                #print("-------------------------\n" + "Team " + str(team.number) + " Got the 4th Place Team Bonus\n---------------------")
                team.coins = team.coins + 25
            timesdone += 1
        
        if (countteams == 3 and timesdone == 1):
            setteams = set()
            for team in teams:
                setteams.add(team.number)
            setteamsin = set(teamsin)
            fourth = setteamsin - setteams
            fourth = list(fourth)
            fourth = fourth[0]
            fourth = int(fourth)
            teamsin = []

            color = ''
            if fourth == 1:
                color = "RED"
            if fourth == 2:
                color = "YELLOW"
            if fourth == 3:
                color = "LIGHTYELLOW_EX"
            if fourth == 4:
                color = "LIGHTGREEN_EX"
            if fourth == 5:
                color = "GREEN"
            if fourth == 6:
                color = "CYAN"
            if fourth == 7:
                color = "LIGHTCYAN_EX"
            if fourth == 8:
                color = "BLUE"
            if fourth == 9:
                color = "MAGENTA"
            if fourth == 10:
                color = "LIGHTRED_EX"
            print(" ︾ " + Style.BRIGHT + getattr(Back, color) + "Team " + str(fourth)  + " Was the fourth full team to finish." + Style.RESET_ALL + " ︽\n")
            for team in teams:
                teamsin.append(team.number)
            for team in teams:
                if (team.number == 1):
                    for player in players:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                if (team.number == 2):
                    for player in players:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                if (team.number == 3):
                    for player in players:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                if (team.number == 4):
                    for player in players:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                if (team.number == 5):
                    for player in players:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                if (team.number == 6):
                    for player in players:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                if (team.number == 7):
                    for player in players:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                if (team.number == 8):
                    for player in players:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                if (team.number == 9):
                    for player in players:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                if (team.number == 10):
                    for player in players:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                team.coins = team.coins + 25 
            timesdone += 1 
        if (countteams == 2 and timesdone == 2):
            setteams = set()
            for team in teams:
                setteams.add(team.number)
            setteamsin = set(teamsin)
            fourth = setteamsin - setteams
            fourth = list(fourth)
            fourth = fourth[0]
            fourth = int(fourth)
            teamsin = []

            color = ''
            if fourth == 1:
                color = "RED"
            if fourth == 2:
                color = "YELLOW"
            if fourth == 3:
                color = "LIGHTYELLOW_EX"
            if fourth == 4:
                color = "LIGHTGREEN_EX"
            if fourth == 5:
                color = "GREEN"
            if fourth == 6:
                color = "CYAN"
            if fourth == 7:
                color = "LIGHTCYAN_EX"
            if fourth == 8:
                color = "BLUE"
            if fourth == 9:
                color = "MAGENTA"
            if fourth == 10:
                color = "LIGHTRED_EX"
            print(" ︾ " + Style.BRIGHT + getattr(Back, color) + "Team " + str(fourth)  + " Was the third full team to finish. " + Style.RESET_ALL + " ︽\n")
            for team in teams:
                teamsin.append(team.number)
            for team in teams:
                if (team.number == 1):
                    for player in players:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                if (team.number == 2):
                    for player in players:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                if (team.number == 3):
                    for player in players:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                if (team.number == 4):
                    for player in players:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                if (team.number == 5):
                    for player in players:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                if (team.number == 6):
                    for player in players:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                if (team.number == 7):
                    for player in players:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                if (team.number == 8):
                    for player in players:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                if (team.number == 9):
                    for player in players:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                if (team.number == 10):
                    for player in players:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                team.coins = team.coins + 25  
            timesdone += 1
        if (countteams == 1 and timesdone == 3):
            setteams = set()
            for team in teams:
                setteams.add(team.number)
            setteamsin = set(teamsin)
            fourth = setteamsin - setteams
            fourth = list(fourth)
            fourth = fourth[0]
            fourth = int(fourth)
            teamsin = []

            color = ''
            if fourth == 1:
                color = "RED"
            if fourth == 2:
                color = "YELLOW"
            if fourth == 3:
                color = "LIGHTYELLOW_EX"
            if fourth == 4:
                color = "LIGHTGREEN_EX"
            if fourth == 5:
                color = "GREEN"
            if fourth == 6:
                color = "CYAN"
            if fourth == 7:
                color = "LIGHTCYAN_EX"
            if fourth == 8:
                color = "BLUE"
            if fourth == 9:
                color = "MAGENTA"
            if fourth == 10:
                color = "LIGHTRED_EX"
            print(" ︾ " + Style.BRIGHT + getattr(Back, color) + "Team " + str(fourth)  + " Was the second full team to finish." + Style.RESET_ALL + " ︽\n")
            for team in teams:
                teamsin.append(team.number)
            for team in teams:
                if (team.number == 1):
                    for player in players:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 1:
                            player.coins = player.coins + 6.25
                if (team.number == 2):
                    for player in players:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 2:
                            player.coins = player.coins + 6.25
                if (team.number == 3):
                    for player in players:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 3:
                            player.coins = player.coins + 6.25
                if (team.number == 4):
                    for player in players:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 4:
                            player.coins = player.coins + 6.25
                if (team.number == 5):
                    for player in players:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 5:
                            player.coins = player.coins + 6.25
                if (team.number == 6):
                    for player in players:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 6:
                            player.coins = player.coins + 6.25
                if (team.number == 7):
                    for player in players:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 7:
                            player.coins = player.coins + 6.25
                if (team.number == 8):
                    for player in players:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 8:
                            player.coins = player.coins + 6.25
                if (team.number == 9):
                    for player in players:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 9:
                            player.coins = player.coins + 6.25
                if (team.number == 10):
                    for player in players:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                    for player in end:
                        if player.team == 10:
                            player.coins = player.coins + 6.25
                setteams = set()
            for team in teams:
                fourth = team.number

            color = ''
            if fourth == 1:
                color = "RED"
            if fourth == 2:
                color = "YELLOW"
            if fourth == 3:
                color = "LIGHTYELLOW_EX"
            if fourth == 4:
                color = "LIGHTGREEN_EX"
            if fourth == 5:
                color = "GREEN"
            if fourth == 6:
                color = "CYAN"
            if fourth == 7:
                color = "LIGHTCYAN_EX"
            if fourth == 8:
                color = "BLUE"
            if fourth == 9:
                color = "MAGENTA"
            if fourth == 10:
                color = "LIGHTRED_EX"
            team.coins = team.coins + 25
            #end2.append(teams[0])
            #teams.pop(0)

            timesdone += 1 
        if (countteams == 0 and timesdone == 4):
            print(" ︾ " + Style.BRIGHT + getattr(Back, color) + "Team " + str(fourth)  + " Was the first full team to finish." + Style.RESET_ALL + " ︽\n")   
            timesdone += 1    
            
        minimum = 10000
        index3 = 0
        index = 0
        index2 = index2 + 1
        count2 = count2 - 1
    sorted = []
    roundsummary = ''
    if round == 6:
        for team in end2:
            roundsummary += ( "Team " + str(team.number) + " Scored " + str(team.coins) + " In Bonuses" + "\n")
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    
    '''for players in final:
        player.coins = math.trunc(player.coins)
        print(math.trunc(players.coins))
    for players in final:
        print(players.name)'''
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 2:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 3:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 4             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 4:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 5             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 5:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 6             ")
        for players in final:
            roundsummary += players.name + "\n"
    if round == 6:
        for players in final:
            roundsummary += str(math.trunc(players.coins)) + "\n"
        for players in final:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")

    return final,roundsummary
    
def Obstacle(players):
    player_0 = Player("null",0,0,0,0,0,0,0)
    player_100 = Player("null",0,0,0,0,0,0,0)
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    minimum = 100000
    last_place = player_0
    first_place = player_100
    end = []
    for player in players:
        count = count + 1
    count2 = 40
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        if count2 == 40:
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 39
            index2 = 1
        if count2 == 39:
            counting = 0
            while (counting < 9):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            index2 = 1
        if count2 == 30:
            counting = 0
            while (counting < 10):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            index2 = 1
        if count2 == 20:
            counting = 0
            while (counting < 2):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 18
            index2 = 1
        if count2 == 18:
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 25
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 17
            index2 = 1
            
        if count2 == 17:
            counting = 0
            while (counting < 3):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2=14
            index2 = 1
        if count2 == 14:
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 55
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 13
            index2 = 1
        if count2 == 13:
            counting = 0
            while (counting < 3):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
            index2 = 1
        if count2 == 10:
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+ " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 9
            index2 = 1
        if count2 == 9:
            counting = 0
            while (counting < 1):
                for player in players:
                    player.coins = player.coins + 70
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team)+  " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 8
            index2 = 1
        if count2 == 8:
            counting = 0
            while (counting < 5):
                for player in players:
                    player.coins = player.coins + 10
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team) + " only scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 3
            index2 = 1
        if count2 == 3:
            counting = 0
            while (counting < 3):
                for player in players:
                    player.coins = player.coins + 70
                    if player.random < minimum:
                        minimum = player.random
                        last_place.name = player.name
                        last_place.random = player.random
                index3 = 0
                for player in players:
                    if player.name == last_place.name:
                        print(player.name + " on team " + str(player.team) + " scored " + str(player.random) + " and was eliminated. " + str(len(players)) + "th place.")
                        end.append(players[index3])
                        players.pop(index3)
                    index3 = index3 + 1
                counting = counting + 1
                minimum = 100000
                count2 = 8
            index2 = 10000
        
            
        minimum = 10000
        index = 0
        count = 20
        if count2 == 3:
            count2 = 2
        if count2 == 5:
            count2 = 3
        if count2 == 10:
            count2 = 5
        if count2 == 13:
            count2 = 10
        if count2 == 30:
            count2 = 20
        if count2 == 39:
            count2 = 30
        print("----------------- REMAINING PLAYERS -----------------")
        for player in players:
            print(str(player.name) + ": On Team " + str(player.team) + " and scored: " + str(player.random)) 
        #normally 15    
        time.sleep(timer*15)
        #usually 20
        

    sorted = []
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    for players in final:
        print(players.coins)
    for players in final:
        print(players.name)
    return final
    
def Parkour1(players,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    player_100 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    minimum = 100000
    last_place = player_0
    first_place = player_100
    end = []
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    for player in players:
        count = count + 1
    count2 = 40
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        for player in players:
            if (player.random > 7 and player.random <= 35):
                player.coins += 25
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got a " + Fore.YELLOW + "bronze medal" + Fore.LIGHTWHITE_EX + " (" + str(player.coins) + " total 🪙 ) [+25🪙 ]")
            if (player.random > 35 and player.random <= 65):
                player.coins += 45
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got a " + Fore.YELLOW + "bronze medal" + Style.RESET_ALL + " and a  silver medal" + Fore.LIGHTWHITE_EX + " (" + str(player.coins) + " total 🪙 ) [+45🪙 ]")
            if player.random > 65:
                player.coins += 70
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got a " + Fore.YELLOW + "bronze medal, " + Style.RESET_ALL  + "silver," + Fore.LIGHTYELLOW_EX + " and gold medal" + Fore.LIGHTWHITE_EX + " (" + str(player.coins) + " total 🪙 ) [+70🪙 ]")
        index2 = 1000000
            
        minimum = 10000
        index = 0
        count = 20
        if count2 == 3:
            count2 = 2
        if count2 == 5:
            count2 = 3
        if count2 == 10:
            count2 = 5
        if count2 == 20:
            count2 = 10
        if count2 == 39:
            count2 = 20

    sorted = []
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    for players in final:
        print(players.coins)
    for players in final:
        print(players.name)
    if round == 1:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
    if round == 2:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 3             ")
    if round == 3:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 4             ")
    if round == 4:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 5             ")
    if round == 5:
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 6             ")
    return players

def Parkour2(players,round):
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    player_100 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    for player in players:
        player.kills = 0
    team1Multiplier = 1
    team2Multiplier = 1
    team3Multiplier = 1
    team4Multiplier = 1
    team5Multiplier = 1
    team6Multiplier = 1
    team7Multiplier = 1
    index4 = 0
    team8Multiplier = 1
    team9Multiplier = 1
    team10Multiplier = 1
    count2 = 0
    minimum = 100000
    last_place = player_0
    first_place = player_100
    end = []
    for player in players:
        count = count + 1
    count2 = 40
    while index2 < count:
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        for player in players:
            if (player.random > 5 and player.random <= 35):
                player.kills = 0.15
                player.coins += 10
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got " + Fore.GREEN + "EASY" + Style.RESET_ALL + " ending")
            if (player.random > 35 and player.random <= 85):
                player.kills = 0.3
                player.coins += 20
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got " + Fore.BLUE + "MEDIUM" + Style.RESET_ALL + " ending")
            if (player.random > 85):
                player.kills = 0.6
                player.coins += 30
                print(getattr(Fore,player.color) + player.name + Style.RESET_ALL +  " got " + Fore.RED + Style.BRIGHT + "HARD" + Style.RESET_ALL + " ending")

    
        
        index2 = 100000
        for player in players:
            if player.team == 1:
                team1Multiplier += player.kills
            if player.team == 2:
                team2Multiplier += player.kills
            if player.team == 3:
                team3Multiplier += player.kills
            if player.team == 4:
                team4Multiplier += player.kills
            if player.team == 5:
                team5Multiplier += player.kills
            if player.team == 6:
                team6Multiplier += player.kills
            if player.team == 7:
                team7Multiplier += player.kills
            if player.team == 8:
                team8Multiplier += player.kills
            if player.team == 9:
                team9Multiplier += player.kills
            if player.team == 10:
                team10Multiplier += player.kills
        roundsummary = ''
        roundsummary += ("Team 1 Multiplier: " + str(team1Multiplier) + "\n")
        roundsummary +=("Team 2 Multiplier: " + str(team2Multiplier)+ "\n")
        roundsummary +=("Team 3 Multiplier: " + str(team3Multiplier)+ "\n")
        roundsummary +=("Team 4 Multiplier: " + str(team4Multiplier)+ "\n")
        roundsummary +=("Team 5 Multiplier: " + str(team5Multiplier)+ "\n")
        roundsummary +=("Team 6 Multiplier: " + str(team6Multiplier)+ "\n")
        roundsummary +=("Team 7 Multiplier: " + str(team7Multiplier)+ "\n")
        roundsummary +=("Team 8 Multiplier: " + str(team8Multiplier)+ "\n")
        roundsummary +=("Team 9 Multiplier: " + str(team9Multiplier)+ "\n")
        roundsummary +=("Team 10 Multiplier: " + str(team10Multiplier)+ "\n")
        for player in players:
            if player.team == 1:
                player.coins = player.coins * team1Multiplier
            if player.team == 2:
                player.coins = player.coins * team2Multiplier
            if player.team == 3:
                player.coins = player.coins * team3Multiplier
            if player.team == 4:
                player.coins = player.coins * team4Multiplier
            if player.team == 5:
                player.coins = player.coins * team5Multiplier
            if player.team == 6:
                player.coins = player.coins * team6Multiplier
            if player.team == 7:
                player.coins = player.coins * team7Multiplier
            if player.team == 8:
                player.coins = player.coins * team8Multiplier
            if player.team == 9:
                player.coins = player.coins * team9Multiplier
            if player.team == 10:
                player.coins = player.coins * team10Multiplier
        index4 = 0
        '''while index4 < 40:
            end.append(players[0])
            players.pop(0)
            index4 = index4 + 1
        '''    
        minimum = 10000
        index = 0
        count = 20
        if count2 == 3:
            count2 = 2
        if count2 == 5:
            count2 = 3
        if count2 == 10:
            count2 = 5
        if count2 == 20:
            count2 = 10
        if count2 == 39:
            count2 = 20
    count7 = 0
    while count7 < 40:
        end.append(players[0])
        players.pop(0)
        count7 += 1
    sorted = []
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    popindex = 0
    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    for player in end:
        roundsummary += (str(math.trunc(player.coins)) + "\n")
    for player in end:
        roundsummary += (player.name + "\n")
    if round == 6:
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")
    return end,roundsummary

def Duels(players,round):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 0
    index = 0
    index2 = 0
    count2 = 0
    lefton1 = 0
    lefton2 = 0
    lefton3 = 0
    lefton4 = 0
    lefton5 = 0
    lefton6 = 0
    lefton7 = 0
    lefton8 = 0
    lefton9 = 0
    lefton10 = 0
    minimum = 100000
    placement = 40
    last_place = player_0
    end = []
    list2 = []
    list2size =0 
    for player in players:
        count = count + 1
        index2 += 1
    count2 = count
    added = False
    print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(round) + " ✧                     ")
    print("")
    while index2 > 1:
        if added == False:
            for player in players:
                list2.append(player)
                list2size += 1
                player.coins += 5
        count = 0
        for player in players:
            count = count + 1
        count2 = count
        index = 0
        while index < count2:
            players[index].random = random.randint(1,players[index].skill)
            index = index + 1
        list2size = 0
        if index2 == 20:
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Final 20  ✧                     ")
            list2 = sorted(list2, key=operator.attrgetter('team'))
            for player in list2:
                print(getattr(Fore,player.color) + player.name + " (" + str(player.team) + ")")
            print("")
            #normally 3
            time.sleep(timer*3)
        if index2 == 10:
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Final 10  ✧                     ")
            list2 = sorted(list2, key=operator.attrgetter('team'))
            for player in list2:
                print(getattr(Fore,player.color) + player.name + " (" + str(player.team) + ")")
            print("")
            #normally 3
            time.sleep(timer*3)
        if index2 == 5:
            print(Style.BRIGHT + Back.BLACK + "                      ✧  Final 5  ✧                     ")
            list2 = sorted(list2, key=operator.attrgetter('team'))
            for player in list2:
                print(getattr(Fore,player.color) + player.name + " (" + str(player.team) + ")")
            print("")
            #normally 3
            time.sleep(timer*3)
        for player in list2:
            list2size += 1
        randomed = random.randint(0,list2size-1)
        player0 = list2[randomed]
        list2.pop(randomed)
        randomed = random.randint(0,list2size-2)
        player1 = list2[randomed]
        list2.pop(randomed)
        print(getattr(Fore,player0.color) + str(player0.name) + Style.RESET_ALL + Style.BRIGHT + Fore.BLACK + " vs " + Style.RESET_ALL + getattr(Fore,player1.color) + str(player1.name))
        #normally 2
        time.sleep(timer*1)
        if (player0.random > player1.random): 
            print(getattr(Fore,player0.color) + str(player0.name) + Style.RESET_ALL + Style.BRIGHT + Fore.BLACK +  " Wins" + Style.RESET_ALL + " [" + getattr(Fore,player1.color) + str(player1.name) + Style.RESET_ALL + " 『" + str(index2) + "』]"+ "\n")
            player0.kills += 1
            list2.append(player0)
            end.append(player1)
        if (player0.random == player1.random):
            print(getattr(Fore,player0.color) + str(player0.name) + Style.RESET_ALL + Style.BRIGHT + Fore.BLACK +  " Wins" + Style.RESET_ALL + " [" + getattr(Fore,player1.color) + str(player1.name) + Style.RESET_ALL + " 『" + str(index2) + "』]"+ "\n")
            player0.kills += 1
            player0.kills += 1
            list2.append(player0)
            end.append(player1)
        if (player1.random > player0.random):
            print(getattr(Fore,player1.color) + str(player1.name) + Style.RESET_ALL + Style.BRIGHT + Fore.BLACK +  " Wins" + Style.RESET_ALL + " [" + getattr(Fore,player0.color) + str(player0.name) + Style.RESET_ALL + " 『" + str(index2) + "』]"+ "\n")
            player1.kills += 1
            list2.append(player1)
            end.append(player0)
        if len(list2) == 1:
            print(getattr(Fore,list2[0].color) + str(list2[0].name) + Style.RESET_ALL + " Wins!")
            end.append(list2[0])
        #normally 2
        time.sleep(timer*1)
        index2 -= 1
        index = 0
        added = True
        lefton1 = 0
        lefton2 = 0
        lefton3 = 0
        lefton4 = 0
        lefton5 = 0
        lefton6 = 0
        lefton7 = 0
        lefton8 = 0
        lefton9 = 0
        lefton10 = 0
        for player in list2:
            if player.team == 1:
                lefton1 += 1
            if player.team == 2:
                lefton2 += 1
            if player.team == 3:
                lefton3 += 1
            if player.team == 4:
                lefton4 += 1
            if player.team == 5:
                lefton5 += 1
            if player.team == 6:
                lefton6 += 1
            if player.team == 7:
                lefton7 += 1
            if player.team == 8:
                lefton8 += 1
            if player.team == 9:
                lefton9 += 1
            if player.team == 10:
                lefton10 += 1
        if index2 > 18:
            for player in list2:
                player.coins += 5
        if index2 == 18:
            for player in list2:
                player.coins += 12
        if index2 > 14 and index2 < 18:
            for player in list2:
                player.coins += 5
        if index2 == 14:
            for player in list2:
                player.coins += 28
        if index2 > 9 and index2 < 14:
            for player in list2:
                player.coins += 5
        if index2 == 9:
            for player in list2:
                player.coins += 35
        if index2 > 3 and index2 < 9:
            for player in list2:
                player.coins += 5
        if index2 <= 3:
            for player in list2:
                player.coins += 35
        print(Style.BRIGHT + Back.BLACK + "                          ✧  Remaining on Teams ✧                         ")
        print(Fore.RED + "1" + Style.RESET_ALL + "       " + Fore.YELLOW + "2" + Style.RESET_ALL + "       " + Fore.LIGHTYELLOW_EX + "3" + Style.RESET_ALL + "       " + 
            Fore.LIGHTGREEN_EX + "4" + Style.RESET_ALL + "       " + Fore.GREEN + "5" + Style.RESET_ALL + "       " + Fore.CYAN + "6" + Style.RESET_ALL + "       " + Fore.LIGHTCYAN_EX + "7" + Style.RESET_ALL + "       " +
            Fore.BLUE + "8" + Style.RESET_ALL + "       " + Fore.MAGENTA + "9" + Style.RESET_ALL + "      " + Fore.LIGHTRED_EX + "10" + Style.RESET_ALL + "       " )
        print(Style.BRIGHT + str(lefton1) + "       " + str(lefton2) + "       " +str(lefton3) + "       " +str(lefton4) + "       " +str(lefton5) + "       " +str(lefton6) + "       " +str(lefton7) + "       " +str(lefton8) + "       " +str(lefton9) + "       " +str(lefton10) + "\n")
            
        #print("1   2   3   4   5   6   7   8   9   10")
        #print(str(lefton1) + "   " + str(lefton2) + "   " +str(lefton3) + "   " +str(lefton4) + "   " +str(lefton5) + "   " +str(lefton6) + "   " +str(lefton7) + "   " +str(lefton8) + "   " +str(lefton9) + "   " +str(lefton10) + "\n")
        
    end.reverse()
    roundsummary = ''
    if round == 1:
        for players in end:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "             Press Enter for Round 2             ")
    if round == 2:
        for players in end:
            roundsummary += str(players.coins) + "\n"
        for players in end:
            roundsummary += players.name + "\n"
        print(Style.BRIGHT + Back.WHITE + "              Press Enter for Stats             ")
    return end,roundsummary

def SOT(players):
    player_0 = Player("null",0,0,0,0,0,0,0,"RED")
    player_100 = Player("null",0,0,0,0,0,0,0,"RED")
    count = 5
    index = 0
    index2 = 0
    count2 = 0
    minimum = 100000
    currentTeam = 0
    team1Coins = 0
    team2Coins = 0
    team3Coins = 0
    team4Coins = 0
    team5Coins = 0
    team6Coins = 0
    team7Coins = 0
    team8Coins = 0
    team9Coins = 0
    numTimes = 0
    team10Coins = 0
    ranomDeath = 1000
    last_place = player_0
    first_place = player_100
    end = []
    count2 = 40
    while index2 < count:
        index = 0
        while index < count2:
            players[index].coins2 = random.randint(1,players[index].skill*2)
            index = index + 1
        ranomDeath = random.randint(0,39)
        print(Style.BRIGHT + Back.BLACK + "                      ✧  Round " +  str(index2+1) + " ✧                     ")
        print("")
        print("⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛")
        print(getattr(Fore, players[ranomDeath].color) +"           " + players[ranomDeath].name + " HAS DIED. Team: " + str(players[ranomDeath].team))
        print("⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛")
        if (players[ranomDeath].team == 1):
            team1Coins = team1Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 2):
            team2Coins = team2Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 3):
            team3Coins = team3Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 4):
            team4Coins = team4Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 5):
            team5Coins = team5Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 6):
            team6Coins = team6Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 7):
            team7Coins = team7Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 8):
            team8Coins = team8Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 9):
            team9Coins = team9Coins - players[ranomDeath].coins
        if (players[ranomDeath].team == 10):
                team10Coins = team10Coins - players[ranomDeath].coins
        players[ranomDeath].coins = 0
        players[ranomDeath].coins2 = 0

        ranomDeath = random.randint(0,39)
        print("⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛")
        print(getattr(Fore, players[ranomDeath].color) + "    " + players[ranomDeath].name + " HAS UNLOCKED A VAULT +75 Coins. Team: " + str(players[ranomDeath].team))
        print("⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛")
        players[ranomDeath].coins2 += 75
        for player in players:
            if (player.team == 1):
                team1Coins = team1Coins + player.coins2
            if (player.team == 2):
                team2Coins = team2Coins + player.coins2
            if (player.team == 3):
                team3Coins = team3Coins + player.coins2
            if (player.team == 4):
                team4Coins = team4Coins + player.coins2
            if (player.team == 5):
                team5Coins = team5Coins + player.coins2
            if (player.team == 6):
                team6Coins = team6Coins + player.coins2
            if (player.team == 7):
                team7Coins = team7Coins + player.coins2
            if (player.team == 8):
                team8Coins = team8Coins + player.coins2
            if (player.team == 9):
                team9Coins = team9Coins + player.coins2
            if (player.team == 10):
                team10Coins = team10Coins + player.coins2
            player.coins = player.coins + player.coins2
             
        for player in players:
            if (currentTeam != player.team):
                print(getattr(Back,player.color) + Style.BRIGHT  + "              ✧  Team " +  str(player.team) + " ✧                  ")
                if player.team == 1:
                    print(Back.BLACK + "           ✦ TEAM COINS: " + str(team1Coins) + " ✦             ")
                if player.team == 2:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team2Coins) + " ✦             ")
                if player.team == 3:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team3Coins) + " ✦             ")
                if player.team == 4:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team4Coins) + " ✦             ")
                if player.team == 5:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team5Coins) + " ✦             ")
                if player.team == 6:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team6Coins) + " ✦             ")
                if player.team == 7:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team7Coins) + " ✦             ")
                if player.team == 8:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team8Coins) + " ✦             ")
                if player.team == 9:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team9Coins) + " ✦             ")
                if player.team == 10:
                    print(Back.BLACK +"           ✦ TEAM COINS: " + str(team10Coins) + " ✦              ")
                currentTeam = player.team
            print(player.name + " has " + str(player.coins) + " Coins. [+" + str(player.coins2) + "🪙 ]")
        player.coins2 = 0  
        index2 = index2 + 1
        index = 10000    
        minimum = 10000
        #normally 20
        time.sleep(timer*10)
        
    looping = 0
    while looping < 40:
        end.append(players[0])
        players.pop(0)
        looping += 1
    sorted = []
    most_coins = 0
    final = player_0
    count4 = 0
    index4 = 0
    index5 = 0
    final = []
    end2 = end
    
    popindex = 0
    individual1 = math.trunc(team1Coins / 4)
    individual2 = math.trunc(team2Coins / 4)
    individual3 = math.trunc(team3Coins / 4)
    individual4 = math.trunc(team4Coins / 4)
    individual5 = math.trunc(team5Coins / 4)
    individual6 = math.trunc(team6Coins / 4)
    individual7 = math.trunc(team7Coins / 4)
    individual8 = math.trunc(team8Coins / 4)
    individual9 = math.trunc(team9Coins / 4)
    individual10 = math.trunc(team10Coins / 4)
    for players in end:
        if (players.team == 1):
            players.coins2 = players.coins
            players.coins = individual1
        if (players.team == 2):
            players.coins2 = players.coins
            players.coins = individual2
        if (players.team == 3):
            players.coins2 = players.coins
            players.coins = individual3
        if (players.team == 4):
            players.coins2 = players.coins
            players.coins = individual4
        if (players.team == 5):
            players.coins2 = players.coins
            players.coins = individual5
        if (players.team == 6):
            players.coins2 = players.coins
            players.coins = individual6
        if (players.team == 7):
            players.coins2 = players.coins
            players.coins = individual7
        if (players.team == 8):
            players.coins2 = players.coins
            players.coins = individual8
        if (players.team == 9):
            players.coins2 = players.coins
            players.coins = individual9
        if (players.team == 10):
            players.coins2 = players.coins
            players.coins = individual10
    while index4 < 40:
        for players in end:
            maximum = 100000
            most = player_0
            index5 = index5 + 1
            if players.coins < maximum:
                maximum = players.coins
                most = players
                popindex = index5 - 1
        if end:
            end.pop(popindex)
            final.append(most)
        index4 = index4 + 1
        index5 = 0
    

    final_list = []
    maximum = 0
    maximum_name = ""
    final_index = 0
    index_append = 0
    index10 = 0
    for players in final:
        print(players.coins)
    for players in final:
        print(players.name)

        





    return final
def DB(players):
    team1number = 0
    team2number = 0
    color1 = ''
    color2 = ''
    team1name = ''
    team2name = ''
    for player in players:
        if team1number == 0:
            team1number = player.team
            color1 = player.color
        if player.team != team1number:
            team2number = player.team
            color2 = player.color
    if color1 == "RED":
        team1name = "Red Rabbits"
    if color1 == "YELLOW":
        team1name = "Orange Ocelots"
    if color1 == "LIGHTYELLOW_EX":
        team1name = "Yellow Yaks"
    if color1 == "LIGHTGREEN_EX":
        team1name = "Lime Llamas"
    if color1 == "GREEN":
        team1name = "Green Geckos"
    if color1 == "CYAN":
        team1name = "Cyan Coyotes"
    if color1 == "LIGHTCYAN_EX":
        team1name = "Aqua Axolotls"
    if color1 == "BLUE":
        team1name = "Blue Bats"
    if color1 == "MAGENTA":
        team1name = "Purple Pandas"
    if color1 == "LIGHTRED_EX":
        team1name = "Pink Parrots"   
    if color2 == "RED":
        team2name = "Red Rabbits"
    if color2 == "YELLOW":
        team2name = "Orange Ocelots"
    if color2 == "LIGHTYELLOW_EX":
        team2name = "Yellow Yaks"
    if color2 == "LIGHTGREEN_EX":
        team2name = "Lime Llamas"
    if color2 == "GREEN":
        team2name = "Green Geckos"
    if color2 == "CYAN":
        team2name = "Cyan Coyotes"
    if color2 == "LIGHTCYAN_EX":
        team2name = "Aqua Axolotls"
    if color2 == "BLUE":
        team2name = "Blue Bats"
    if color2 == "MAGENTA":
        team2name = "Purple Pandas"
    if color2 == "LIGHTRED_EX":
        team2name = "Pink Parrots" 
    team1 = []
    team2 = []
    
    team1shot = []
    team2shot = []
    team1arrows = 0
    team2arrows = 0
    for player in players:
        if player.team == team1number:
            team1.append(player)
        if player.team == team2number:
            team2.append(player)
    team1wins = 0
    team2wins = 0
    goesfirst = 0
    game = False
    while (team1wins != 3 and team2wins != 3):
        team1arrows += 1
        team2arrows += 1
        goesfirst = random.randint(0,1)
        if goesfirst == 0:
            while team1arrows > 0:
                picked = random.randint(0,len(team1)-1)
                accuracy = random.randint(0,team1[picked].skill)%50%30
                if accuracy > 10:
                    eliminated = random.randint(0,len(team2)-1)
                    print(getattr(Fore, team2[eliminated].color) + str(team2[eliminated].name) + Style.RESET_ALL + " was shot by " + getattr(Fore, team1[picked].color) + str(team1[picked].name))
                    team2shot.append(team2[eliminated])
                    team2.pop(eliminated)
                if accuracy <= 10:
                    print(getattr(Fore, team1[picked].color) + str(team1[picked].name) + Style.RESET_ALL + " missed")
                time.sleep(timer*2)

                team1arrows -= 1
                team2arrows += 1
        if goesfirst == 1:
            while team2arrows > 0:
                picked = random.randint(0,len(team2)-1)
                accuracy = random.randint(0,team2[picked].skill)%50%30
                if accuracy > 10:
                    eliminated = random.randint(0,len(team1)-1)
                    print(getattr(Fore, team1[eliminated].color) + str(team1[eliminated].name) + Style.RESET_ALL + " was shot by " + getattr(Fore, team2[picked].color) + str(team2[picked].name))
                    team1shot.append(team1[eliminated])
                    team1.pop(eliminated)
                if accuracy <= 10:
                    print(getattr(Fore, team2[picked].color) + str(team2[picked].name) + Style.RESET_ALL + " missed")
                time.sleep(timer*2)
                team2arrows -= 1
                team1arrows += 1
        while (len(team1) > 0 and len(team2) > 0):
            if team1arrows == 2  and len(team1) > 0:
                while team1arrows > 0 and len(team2) > 0:
                    picked = random.randint(0,len(team1)-1)
                    accuracy = random.randint(0,team1[picked].skill)%50%30
                    if accuracy > 10:
                        eliminated = random.randint(0,len(team2)-1)
                        print(getattr(Fore, team2[eliminated].color) + str(team2[eliminated].name) + Style.RESET_ALL + " was shot by " + getattr(Fore, team1[picked].color) + str(team1[picked].name))
                        team2shot.append(team2[eliminated])
                        team2.pop(eliminated)
                    if accuracy <= 10:
                        print(getattr(Fore, team1[picked].color) + str(team1[picked].name) + Style.RESET_ALL + " missed")
                    time.sleep(timer*2)
                    team1arrows -= 1
                    team2arrows += 1
            if team2arrows == 2 and len(team2) > 0:
                while team2arrows > 0 and len(team1) > 0 :
                    picked = random.randint(0,len(team2)-1)
                    accuracy = random.randint(0,team2[picked].skill)%50%30
                    if accuracy > 10:
                        eliminated = random.randint(0,len(team1)-1)
                        print(getattr(Fore, team1[eliminated].color) + str(team1[eliminated].name) + Style.RESET_ALL + " was shot by " + getattr(Fore, team2[picked].color) + str(team2[picked].name))
                        team1shot.append(team1[eliminated])
                        team1.pop(eliminated)
                    if accuracy <= 10:
                        print(getattr(Fore, team2[picked].color) + str(team2[picked].name) + Style.RESET_ALL + " missed")
                    time.sleep(timer*2)
                    team2arrows -= 1
                    team1arrows += 1
            if len(team1) == 0:
                team2wins += 1
            if len(team2) == 0:
                team1wins += 1
        print(Style.BRIGHT + "Team " + str(team1number) + " round wins: " + str(team1wins))
        print(Style.BRIGHT + "Team "+ str(team2number) +  " round wins: " + str(team2wins))
        team1arrows = 0
        team2arrows = 0
        team1.extend(x for x in team1shot if x not in team1)
        team2.extend(x for x in team2shot if x not in team2)
        if team1wins == 3:
            print(getattr(Back,color1) + "                     " + getattr(Back,color2) + "                       ")
            print(getattr(Fore,color1) + "       " + str(team1name)+ " Are The Champions!")
            print(getattr(Back,color1) + "                     " + getattr(Back,color2) + "                       ")
        if team2wins == 3:
            print(getattr(Back,color2) + "                     " + getattr(Back,color1) + "                       ")
            print(getattr(Fore,color2) + "       " + str(team2name)+ " Are The Champions!")
            print(getattr(Back,color2) + "                     " + getattr(Back,color1) + "                       ")
        keyboardinput = 'AAA'
        while keyboardinput != "":
            keyboardinput = input()

    


def main():
    multiplier = 1
    games = ["TGTTOS", "Sky Battle", "Survival Games", "HITW", "Parkour Warrior", "Sands of Time", "Duels", "RSR", "Disco"]
    count = 1
    team_1x = Team(1,50,0,0,0,"Red Rabbits","RED")
    team_2x = Team(2,50,0,0,0,"Orange Ocelots","YELLOW")
    team_3x = Team(3,50,0,0,0,"Yellow Yaks","LIGHTYELLOW_EX")
    team_4x = Team(4,50,0,0,0,"Lime Llamas","LIGHTGREEN_EX")
    team_5x = Team(5,50,0,0,0,"Green Geckos","GREEN")
    team_6x = Team(6,50,0,0,0,"Cyan Coyotes","CYAN")
    team_7x = Team(7,50,0,0,0,"Aqua Axolotls","LIGHTCYAN_EX")
    team_8x = Team(8,50,0,0,0,"Blue Bats","BLUE")
    team_9x = Team(9,50,0,0,0,"Purple Pandas","MAGENTA")
    team_10x = Team(10,50,0,0,0,"Pink Parrots","LIGHTRED_EX")
    teams = [team_1x, team_2x,team_3x,team_4x,team_5x,team_6x,team_7x,team_8x,team_9x,team_10x]
    team_1xt = Team(1,50,0,0,0,"Red Rabbits","RED")
    team_2xt = Team(2,50,0,0,0,"Orange Ocelots","YELLOW")
    team_3xt = Team(3,50,0,0,0,"Yellow Yaks","LIGHTYELLOW_EX")
    team_4xt = Team(4,50,0,0,0,"Lime Llamas","LIGHTGREEN_EX")
    team_5xt = Team(5,50,0,0,0,"Green Geckos","GREEN")
    team_6xt = Team(6,50,0,0,0,"Cyan Coyotes","CYAN")
    team_7xt = Team(7,50,0,0,0,"Aqua Axolotls","LIGHTCYAN_EX")
    team_8xt = Team(8,50,0,0,0,"Blue Bats","BLUE")
    team_9xt = Team(9,50,0,0,0,"Purple Pandas","MAGENTA")
    team_10xt = Team(10,50,0,0,0,"Pink Parrots","LIGHTRED_EX")
    teamsTGTTOS = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    teamsTGTTOS2 = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    teamsTGTTOS3 = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    teamsTGTTOS4 = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    teamsTGTTOS5 = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    teamsTGTTOS6 = [team_1xt, team_2xt,team_3xt,team_4xt,team_5xt,team_6xt,team_7xt,team_8xt,team_9xt,team_10xt]
    team_1xtg = Team(1,50,0,0,0,"Red Rabbits","RED")
    team_2xtg = Team(2,50,0,0,0,"Orange Ocelots","YELLOW")
    team_3xtg = Team(3,50,0,0,0,"Yellow Yaks","LIGHTYELLOW_EX")
    team_4xtg = Team(4,50,0,0,0,"Lime Llamas","LIGHTGREEN_EX")
    team_5xtg = Team(5,50,0,0,0,"Green Geckos","GREEN")
    team_6xtg = Team(6,50,0,0,0,"Cyan Coyotes","CYAN")
    team_7xtg = Team(7,50,0,0,0,"Aqua Axolotls","LIGHTCYAN_EX")
    team_8xtg = Team(8,50,0,0,0,"Blue Bats","BLUE")
    team_9xtg = Team(9,50,0,0,0,"Purple Pandas","MAGENTA")
    team_10xtg = Team(10,50,0,0,0,"Pink Parrots","LIGHTRED_EX")
    teamsGR = [team_1xtg, team_2xtg,team_3xtg,team_4xtg,team_5xtg,team_6xtg,team_7xtg,team_8xtg,team_9xtg,team_10xtg]
    player_1= Player('player1',80,0,0,0,1,0,0,'RED')
    player_2= Player('player2',80,0,0,0,1,0,0,'RED')
    player_3= Player('player3',60,0,0,0,1,0,0,'RED')
    player_4= Player('player4',40,0,0,0,1,0,0,'RED')
    player_5= Player('player5',80,0,0,0,2,0,0,'YELLOW')
    player_6= Player('player6',40,0,0,0,2,0,0,'YELLOW')
    player_7= Player('player7',60,0,0,0,2,0,0,'YELLOW')
    player_8= Player('player8',60,0,0,0,2,0,0,'YELLOW')
    player_9= Player('player9',100,0,0,0,3,0,0,'LIGHTYELLOW_EX')
    player_10= Player('player10',80,0,0,0,3,0,0,'LIGHTYELLOW_EX')
    player_11= Player('player11',40,0,0,0,3,0,0,'LIGHTYELLOW_EX')
    player_12= Player('player12',40,0,0,0,3,0,0,'LIGHTYELLOW_EX')
    player_13= Player('player13',100,0,0,0,4,0,0,'LIGHTGREEN_EX')
    player_14= Player('player14',80,0,0,0,4,0,0,'LIGHTGREEN_EX')
    player_15= Player('player15',60,0,0,0,4,0,0,'LIGHTGREEN_EX')
    player_16= Player('player16',20,0,0,0,4,0,0,'LIGHTGREEN_EX')
    player_17= Player('player17',100,0,0,0,5,0,0,'BLUE')
    player_18= Player('player18',100,0,0,0,5,0,0,'BLUE')
    player_19= Player('player19',40,0,0,0,5,0,0,'BLUE')
    player_20= Player('player20',20,0,0,0,5,0,0,'BLUE')
    player_21= Player('player21',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
    player_22= Player('player22',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
    player_23= Player('player23',80,0,0,0,6,0,0,'LIGHTCYAN_EX')
    player_24= Player('player24',20,0,0,0,6,0,0,'LIGHTCYAN_EX')
    player_25= Player('player25',100,0,0,0,7,0,0,'CYAN')
    player_26= Player('player26',60,0,0,0,7,0,0,'CYAN')
    player_27= Player('player27',60,0,0,0,7,0,0,'CYAN')
    player_28= Player('player28',20,0,0,0,7,0,0,'CYAN')
    player_29= Player('player29',100,0,0,0,8,0,0,'MAGENTA')
    player_30= Player('player30',80,0,0,0,8,0,0,'MAGENTA')
    player_31= Player('player31',60,0,0,0,8,0,0,'MAGENTA')
    player_32= Player('player32',20,0,0,0,8,0,0,'MAGENTA')
    player_33= Player('player33',80,0,0,0,9,0,0,'LIGHTRED_EX')
    player_34= Player('player34',60,0,0,0,9,0,0,'LIGHTRED_EX')
    player_35= Player('player35',60,0,0,0,9,0,0,'LIGHTRED_EX')
    player_36= Player('player36',40,0,0,0,9,0,0,'LIGHTRED_EX')
    player_37= Player('player37',60,0,0,0,10,0,0,'GREEN')
    player_38= Player('player38',60,0,0,0,10,0,0,'GREEN')
    player_39= Player('player39',60,0,0,0,10,0,0,'GREEN')
    player_40= Player('player40',60,0,0,0,10,0,0,'GREEN')
    team_1 = [player_1,player_2,player_3,player_4]
    team_2 = [player_5,player_6,player_7,player_8]
    team_3 = [player_9,player_10,player_11,player_12]
    team_4 = [player_13,player_14,player_15,player_16]
    team_5 = [player_17,player_18,player_19,player_20]
    team_6 = [player_21,player_22,player_23,player_24]
    team_7 = [player_25,player_26,player_27,player_28]
    team_8 = [player_29,player_30,player_31,player_32]
    team_9 = [player_33,player_34,player_35,player_36]
    team_10 = [player_37,player_38,player_39,player_40]
    end_round = 1
    teamsSG = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10]
    playing = [player_1	, player_2,	player_3	,player_4,	player_5	,player_6,	player_7,	player_8,	player_9,	player_10,
            player_11,	player_12,	player_13,	player_14,	player_15,	player_16,	player_17,	player_18,	player_19,	player_20,
            player_21,	player_22,	player_23,	player_24,	player_25,	player_26,	player_27,	player_28,	player_29,	player_30,
            player_31,	player_32,	player_33,	player_34,	player_35,	player_36,	player_37,	player_38,	player_39,	player_40]
    while count < 9:
        for player in playing:
            player.kills = 0
        game_choser = random.randint(0,9-count)
        if count == 2:
            multiplier = 1.5
        if count == 4:
            multiplier = 2
        if count == 6:
            multiplier = 2.5
        if count == 8:
            multiplier = 3
        for people in playing:
            people.kills = 0

        
        if (games[game_choser] == "TGTTOS"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": TGTTOS")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            """playing = TGTTOS(playing,teamsTGTTOS,1)
            time.sleep(20)
            playing = TGTTOS(playing,teamsTGTTOS2,2)
            time.sleep(20)
            playing = TGTTOS(playing,teamsTGTTOS3,3)
            time.sleep(20)
            playing = TGTTOS(playing,teamsTGTTOS4,4)
            time.sleep(20)
            playing = TGTTOS(playing,teamsTGTTOS5,5)
            time.sleep(20)
            playing = TGTTOS(playing,teamsTGTTOS6,6)"""
            end_round = 1
            playing,roundsummary1 = TGTTOS(playing,teamsTGTTOS,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = TGTTOS(playing,teamsTGTTOS2,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary3 = TGTTOS(playing,teamsTGTTOS3,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary4 = TGTTOS(playing,teamsTGTTOS4,4)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary5 = TGTTOS(playing,teamsTGTTOS5,5)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary6 = TGTTOS(playing,teamsTGTTOS6,6)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)

            print(roundsummary1)
            print(roundsummary2)
            print(roundsummary3)
            print(roundsummary4) 
            print(roundsummary5) 
            print(roundsummary6)
            end_round = 3  
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "Sky Battle"):
            print("Game " + str(count) + ": Sky Battle")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            '''playing = SB(playing,1)
            time.sleep(20)
            playing = SB(playing,2)
            time.sleep(20)
            playing = SB(playing,3)'''
            
            playing,roundsummary1 =SB(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = SB(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary3 = SB(playing,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()

            print(roundsummary1)
            print(roundsummary2)
            print(roundsummary3)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "Survival Games"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": Survival Games")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing = SG(teamsSG)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "HITW"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": HITW")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            '''playing = HITW(playing,1)
            time.sleep(20)
            playing = HITW(playing,2)
            time.sleep(20)
            playing = HITW(playing,3)'''
            playing,roundsummary1 =HITW(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = HITW(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary3 = HITW(playing,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()

            print(roundsummary1)
            print(roundsummary2)
            print(roundsummary3)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "Parkour Warrior"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": Parkour Warrior")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            """playing = Parkour1(playing,1)
            time.sleep(20)
            playing = Parkour1(playing,2)
            time.sleep(20)
            playing = Parkour1(playing,3)
            time.sleep(10)
            playing = Parkour1(playing,4)
            time.sleep(10)
            playing = Parkour1(playing,5)
            time.sleep(20)
            playing = Parkour2(playing,6)"""
            playing = Parkour1(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing = Parkour1(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing = Parkour1(playing,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing = Parkour1(playing,4)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing = Parkour1(playing,5)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary1 = Parkour2(playing,6)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            print(roundsummary1)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "Sands of Time"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": Sands of Time")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing =  SOT(playing)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        '''if (games[game_choser] == "Obstacle"):
            playing = sorted(playing, key=operator.attrgetter('team'))
            print("Game " + str(count) + ": Obstacle")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing  = Obstacle(playing)
            team_total(playing,multiplier,teams)'''
        if (games[game_choser] == "Duels"):
            print("Game " + str(count) + ": Duels")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing,roundsummary1 = Duels(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = Duels(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()

            print(roundsummary1)
            print(roundsummary2)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "Disco"):
            print("Game " + str(count) + ": Disco")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing,roundsummary1 = Disco(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = Disco(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary3 = Disco(playing,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()

            print(roundsummary1)
            print(roundsummary2)
            print(roundsummary3)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
        if (games[game_choser] == "RSR"):
            print("Game " + str(count) + ": RSR")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            """playing =RSR(playing,1)
            time.sleep(20)
            playing = RSR(playing,2)
            time.sleep(20)
            playing = RSR(playing,3)"""
            playing,roundsummary1 =RSR(playing,1)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary2 = RSR(playing,2)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                if keyboardinput == " ":
                    team_total(playing,teams,multiplier,end_round)
                keyboardinput = input()
            time.sleep(timer*2)
            playing,roundsummary3 = RSR(playing,3)
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()

            print(roundsummary1)
            print(roundsummary2)
            print(roundsummary3)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1
            
        if (games[game_choser] == "Grid Runners"):
            print("Game " + str(count) + ": Grid Runners")
            print("Press Enter to Start")
            keyboardinput = 'AAA'
            while keyboardinput != "":
                keyboardinput = input()
            playing = GR(teamsGR,playing)
            end_round = 3
            team_total(playing,teams,multiplier,end_round)
            end_round = 1

        games.pop(game_choser)
        sorted_z = sorted(playing, key=operator.attrgetter('coins'))
        sorted_z.reverse()
        placements = 1
        for people in sorted_z:
            print(Style.BRIGHT + str(placements) + ": " + Style.RESET_ALL + getattr(Fore, people.color) + str(people.name) + Style.RESET_ALL + " Coins: " + str(math.trunc(people.coins)))
            placements += 1
        print("------------")
        for player in playing:
            player.total_coins += player.coins
            player.coins = 0
        count = count + 1
        sorted_y = sorted(teams, key=operator.attrgetter('total_coins'))
        sorted_y.reverse()
        sorted_x = sorted(playing, key=operator.attrgetter('total_coins'))
        sorted_x.reverse()
        for team in sorted_y:
            print(getattr(Fore, team.color) +  str(team.name) + Style.RESET_ALL + " Coins: " + str(math.trunc(team.total_coins)))
        print("------------")
        placements = 1
        for people in sorted_x:
            print(Style.BRIGHT + str(placements) + ": " + Style.RESET_ALL + getattr(Fore, people.color) + str(people.name) + Style.RESET_ALL + " Coins: "  + str(math.trunc(people.total_coins)))
            placements += 1
            
        print("------------")
        print("Remaining Games:" + str(games))
        print("Press Enter to Continue")
        keyboardinput = 'AAA'
        while keyboardinput != "":
            keyboardinput = input()
    team1dodgebolt = 0
    team2dodgebolt = 0
    countdb = 0
    dodgeboltteams = []
    for team in sorted_y:
        if countdb < 1:
            team1dodgebolt = team.number
        if countdb == 1:
            team2dodgebolt = team.number
        countdb += 1
    for players in playing:
        if players.team == team1dodgebolt or players.team == team2dodgebolt:
            dodgeboltteams.append(players)
    DB(dodgeboltteams)

main()

            








