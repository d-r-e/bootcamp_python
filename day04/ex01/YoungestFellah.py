#!/usr/bin/env python3

from FileLoader import FileLoader
import pandas as pd

def youngestFellah(df, year):
    female = df['Age'].loc[df['Sex'] == 'F'].loc[df['Year'] == year].min(0)
    male = df['Age'].loc[df['Sex'] == 'M'].loc[df['Year'] == year].min(0)
    return {'f': female, 'm': male}
if __name__ == "__main__":
    data = FileLoader.load("../resources/athlete_events.csv")
    print(youngestFellah(data, 2004))