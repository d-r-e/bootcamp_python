#! /usr/bin/env python3
import pandas as pd

class FileLoader:
    @staticmethod
    def load(path):
        data = pd.read_csv(path)
        print("Loading dataset of dimensions "
               + "{} x {}".format(data.shape[0], data.shape[1]))
        return data
    
    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))

if __name__ == "__main__":
    data = FileLoader.load("../resources/athlete_events.csv")
    FileLoader.display(data, -4)
    FileLoader.display(data, 6)