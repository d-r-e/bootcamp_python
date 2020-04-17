#! /usr/bin/env python3

from FileLoader import FileLoader


def howManyMedals(df, name):
    person = df.loc[df.Name == name, ['Year', 'Medal']]
    ret = {}
    for index, row in person.iterrows():
        ret[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == 'Gold':
            ret[row['Year']]['G'] += 1
        elif row['Medal'] == 'Silver':
            ret[row['Year']]['S'] += 1
        elif row['Medal'] == 'Bronze':
            ret[row['Year']]['B'] += 1
    return ret


if __name__ == "__main__":
    df = FileLoader.load("../resources/athlete_events.csv")
    print(howManyMedals(df, 'Kjetil Andr Aamodt'))
