#! /usr/bin/env python3

from FileLoader import FileLoader


class SpatioTemporalData:

    def __init__(self, df):
        self.df = df

    def when(self, loc):
        year = self.df.loc[self.df['City'] == loc]['Year'].drop_duplicates()
        return year.to_list()

    def where(self, date):
        city = self.df.loc[self.df['Year'] == date]['City'].drop_duplicates()
        return city.to_list()


if __name__ == "__main__":
    data = FileLoader.load("../resources/athlete_events.csv")
    std = SpatioTemporalData(data)
    print(std.when('Paris'))
    print(std.where(2016))
