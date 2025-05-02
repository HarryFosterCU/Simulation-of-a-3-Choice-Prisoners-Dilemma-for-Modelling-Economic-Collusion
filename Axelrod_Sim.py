import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import Strategy as st


class Player:
    def __init__(self, Strat, Name):
        self.Response = Strat
        self.Total_Points = 0
        self.Name = Name
        self.Times_Player = 0

def Get_Players():
    #Creates a player for each strategy. Returns list of these players
    Strats = st.Get_All_Strats()
    Names = st.Get_All_Names()
    Players = []

    for A in range(len(Strats)):
        Players.append(Player(Strats[A], Names[A]))
    return(Players)

def Axelrod_Single(Months, Player1, Player2, Payoff_Matrix, test_count):
    #Plays a single run of the Axelrod game (repeated)
    P1_Play_Hist = []
    P2_Play_Hist = []
    P1_Sum = 0
    P2_Sum = 0
    for x in range(Months):
        #print(x)
        P1Resp = Player1.Response(P2_Play_Hist)
        P2Resp = Player2.Response(P1_Play_Hist)  #Temporary storage so that they will play simultaneously
        P1_Play_Hist.append(P1Resp)
        P2_Play_Hist.append(P2Resp)
        Player1.Total_Points += (Payoff_Matrix[P1_Play_Hist[x]])[P2_Play_Hist[x]]
        P1_Sum += (Payoff_Matrix[P1_Play_Hist[x]])[P2_Play_Hist[x]]
        Player2.Total_Points += (Payoff_Matrix[P2_Play_Hist[x]])[P1_Play_Hist[x]]
        P2_Sum += (Payoff_Matrix[P2_Play_Hist[x]])[P1_Play_Hist[x]]
        if P1_Play_Hist[x] == 2:
            break
        elif P2_Play_Hist[x] == 2:
            break
    return([P1_Sum, P2_Sum, Player1.Name, Player2.Name])
    
def Full_Game(Time, Payoff_Matrix):
    #Plays the entire game
    m = 0
    Players = Get_Players()
    Final_Profit = {}
    H2H = []
    for i in Players:
        for j in Players:
            Versus_Sum = Axelrod_Single(Time, i, j, Payoff_Matrix, m)
            H2H.append(Versus_Sum)
    for A in Players:
        Final_Profit[A.Name] = A.Total_Points
    Final_Profit = dict(sorted(Final_Profit.items(), key=lambda item: item[1], reverse=True))
    return(Final_Profit, H2H)

def Show_Player_Scores(Time, Payoff_Matrix):
    #displays the scores of each group.
    Sim_Results = Full_Game(Time, Payoff_Matrix)
    for (x,y) in Sim_Results[0].items():
        print(x, y)