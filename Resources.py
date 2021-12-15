import pandas as pd
import numpy as np

def checkForAuthor(journalAuthors, lastName):
    if (journalAuthors.find(lastName) == -1):
        return False
    else:
        return True

def getTitlesWithAuthors():
    df = pd.read_excel(r'resources\Oct 2021.xlsx')
    titles = pd.DataFrame(df, columns = ['Authors', 'Title', 'Journal'])
    titles_authors = titles.values
    return titles_authors

def getAgents():
    f = open("resources\\agents.txt")
    agents = f.readlines()
    for i in range(len(agents)):
        agents[i] = agents[i].rstrip()
    return agents

def getPumps():
    f = open("resources\\pumps.txt")
    pumps = f.readlines()
    for i in range(len(pumps)):
        pumps[i] = pumps[i].rstrip()
    return pumps

def getRoutes():
    f = open("resources\\routes.txt")
    routes = f.readlines()
    for i in range(len(routes)):
        routes[i] = routes[i].rstrip()
    while '' in routes: 
        routes.remove('')    
    return routes

def getVehicles():
    f = open("resources\\vehicles.txt")
    vehicles = f.readlines()
    for i in range(len(vehicles)):
        vehicles[i] = vehicles[i].rstrip()
    return vehicles

def getKits():
    f = open("resources\\kits.txt")
    kits = f.readlines()
    for i in range(len(kits)):
        kits[i] = kits[i].rstrip()
    return kits

