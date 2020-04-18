#! /usr/bin/env python3

from FileLoader import FileLoader
import pandas as pd


def howManyMedalsByCountry(df, name):
    country = df.loc[df['Team'] == name]
    dic = {}
    for index, row in country.iterrows():
        dic[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == 'Gold':
            dic[row['Year']]['G'] += 1
        if row['Medal'] == 'Silver':
            dic[row['Year']]['S'] += 1
        if row['Medal'] == 'Bronze':
            dic[row['Year']]['B'] += 1
    return dic


if __name__ == "__main__":
    df = FileLoader.load("../resources/athlete_events.csv")
    print(howManyMedalsByCountry(df, 'China'))
