import numpy as np
from numpy import random

def Always_Coop(Play_Hist): #Always Cooperates
    return(0)
def Always_Report(Play_Hist):#Reports turn 1 (Limiting strategy)
    return(2)
def Always_Defect(Play_Hist):#Always Defects
    return(1)
def Tit_For_Tat(Play_Hist): #Cooperates until opponent defects, then copies their last move each round
    if len(Play_Hist) == 0:
        return(0)
    elif Play_Hist[len(Play_Hist) - 1] == 1:
        return(1)
    else:
        return(0)
def Two_Tit_For_Tat(Play_Hist): #Cooperates, defects twice if opponent defects once
    if len(Play_Hist) == 0:
        return(0)
    elif Play_Hist[len(Play_Hist) - 1] == 1:
        return(1)
    elif Play_Hist[len(Play_Hist) - 2] == 1:
        return(1)
    else:
        return(0)


def Three_Month(Play_Hist): #Coop -> Defect -> report
    if len(Play_Hist) == 0:
        return(0)
    elif len(Play_Hist) == 1:
        return(1)
    elif len(Play_Hist) == 2:
        return(2)

def Quick_Profit(Play_Hist): #Defect -> report
    if len(Play_Hist) == 0:
        return(1)
    elif len(Play_Hist) == 1:
        return(2)
    
def Two_Tit(Play_Hist): #Defects if opponent defects twice in a row
    if len(Play_Hist) == 0:
        return(0)
    elif Play_Hist[len(Play_Hist) - 1] == 1:
        if Play_Hist[len(Play_Hist) - 2] == 1:
            return(1)
    else:
        return(0)

def Big_Grudger(Play_Hist): #If opponent defects, report
    if len(Play_Hist) < 2:
        return(0)
    elif Play_Hist[len(Play_Hist) - 1] == 2:
        return(2)
    else:
        return(0)

def Random_Until_Seven(Play_Hist): #Play randomly until turn 8 when it reports for no reason
    if len(Play_Hist) == 7:
        return(2)
    else:
        return(random.choice([0, 1], p=(0.5, 0.5), size=(1))[0])
        
    
def Tit_For_Big_Tat(Play_Hist): #If opponent defects, defect and then report
    if len(Play_Hist) <= 2:
        return(0)
    elif Play_Hist[len(Play_Hist)-2] == 1:
        return(2)
    elif Play_Hist[len(Play_Hist)-1] == 1:
        return(1)
    else:
        return(0)
    
def Grudge(Play_Hist): #If opponent defects, defect for rest of the game
    if 1 in Play_Hist:
        return(1)
    else:
        return(0)

def Fool_Me_Once(Play_Hist): #If opponent has defected twice this game, report
    k = 0
    for n in Play_Hist:
        if n == 1:
            k += 1
    if k >= 2:
        return(2)
    else:
        return(0)

def Patient_Grudger(Play_Hist): #If opponent has defected twice or more this game, defect for the rest of the game
    k = 0
    for n in Play_Hist:
        if n == 1:
            k += 1
    if k >= 2:
        return(1)
    else:
        return(0)


def Lose_Your_Mind(Play_Hist): #Cooperate until turn 10, then defect twice and report on the final round
    if len(Play_Hist) == 9:
        return(1)
    elif len(Play_Hist) == 10:
        return(1)
    elif len(Play_Hist) == 11:
        return(2)
    else:
        return(0)
    
def Nice_Thrice_a_Year(Play_Hist): #Be nice on round 1 and every 3rd round. Otherwise, defect
    if len(Play_Hist)%3 == 0:
        return(0)
    else:
        return(1)
    
def Shameful(Play_Hist): #Defect until turn 5. Afterwards, report if they are being nice, report if they are being nasty
    Times_Defected = 0
    Times_Nice = 0
    for i in Play_Hist:
        if i == 0:
            Times_Nice += 1
        else:
            Times_Defected += 1
    if len(Play_Hist) >= 5:
        if Times_Defected > Times_Nice:
            return(2)
        else:
            return(1)
    else:
        return(1)
    

def Get_All_Strats():
    #Returns an array of all strategy functions
    return([Always_Coop, Always_Report, Always_Defect, Tit_For_Tat, Two_Tit_For_Tat, Three_Month,
           Quick_Profit, Big_Grudger, Random_Until_Seven, Tit_For_Big_Tat, Grudge, Fool_Me_Once, Patient_Grudger, Lose_Your_Mind, Nice_Thrice_a_Year,
           Shameful])

def Get_All_Names():
    #Returns an array of all strategy names
    return(["Always Coop", "Always Report", "Always Defect", "Tit For Tat", "Two Tits For a Tat", "Three Month Plan", "Quick Profit",
            "Big Grudger", "Random_Until_Seven", "Tit For Big Tat", "Grudger", "Fool Me Once", "Patient Grudger", "9 Month Plan",
            "Nice Thrice a Year", "Shameful"])
