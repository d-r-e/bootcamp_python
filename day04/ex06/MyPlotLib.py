#! /usr/bin/env python 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
    
    @staticmethod
    def histogram(data, features):
        data = data.dropna()
        if 'Height' in features:
            plt.subplot(1, 2, 1)
            height = data[['Height']].to_numpy()
            plt.hist(height, bins=int(max(height)-min(height)), color ='gold', label='Heigth')
            plt.legend()
        if 'Weight' in features:
            plt.subplot(1, 2, 2)
            weight = data[['Weight']].to_numpy()
            plt.hist(weight, bins=int(max(weight)-min(weight)), label='Width')
            plt.legend()
        plt.show()
        return
    
    @staticmethod
    def density(data, features):
        data = data.dropna()
        if 'Height' in features:
            height = data[['Height']].to_numpy()
            h = plt.hist(height, bins=int(max(height)-min(height)), density=True, histtype='step', label='Height')
        if 'Weight' in features:
            weight = data[['Weight']].to_numpy()
            w = plt.hist(weight, bins=int(max(weight)-min(weight)), histtype='step', density=True, label='Width')
        plt.legend()
        plt.show()
        return
    
    @staticmethod
    def pair_plot(data, features):
        data = data.dropna()
        height = data[['Height']].to_numpy()
        weight = data[['Weight']].to_numpy()
        fig, axes = plt.subplots(2, 2)
        axes[0, 0].hist(height, bins=int(max(height)-min(height)), color='pink')
        axes[1, 0].scatter(height, weight)
        axes[1, 1].hist(weight, bins=int(max(weight)-min(weight)), color='olive')
        axes[0, 1].scatter(weight, height)
        axes[0, 0].set_ylabel('Height')
        axes[1, 0].set_ylabel('Weigth')
        plt.show()
        return
    
    def box_plot(data, features):
        weight = data[['Weight']]
        height = data[['Height']]
        hplot = sns.boxplot(weight)
        wplot = sns.boxplot(height)
        wplot.set(xlabel = 'Height vs Weight')
        return
        
