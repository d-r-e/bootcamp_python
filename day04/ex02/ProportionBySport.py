#!/usr/bin/env python3
from FileLoader import FileLoader
import pandas as pd

def proportionBySport(df, year, sport, sex):
    total = df.loc[df['Year'] == year].loc[df['Sex'] == sex]
    portion = df.loc[df['Year'] == year].loc[df['Sport'] == sport].loc[df['Sex'] == sex]
    total = total['ID'].drop_duplicates(keep='first').count()
    portion = portion['ID'].drop_duplicates(keep='first').count()
    return portion / total


if __name__ == "__main__":
    data = FileLoader.load('../resources/athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F'))