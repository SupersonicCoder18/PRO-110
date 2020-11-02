import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
Clap = df["claps"].to_list()

ClapMean = statistics.mean(Clap)
ClapMedian = statistics.median(Clap)
ClapMode = statistics.mode(Clap)
ClapStdev = statistics.stdev(Clap)

fig = ff.create_distplot([Clap], ["Claps"], show_hist = False)

def RandomSetOfMean(counter):
    DataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(Clap) - 1)
        value = Clap[randomIndex]
        DataSet.append(value)
    mean = statistics.mean(DataSet)
    return mean

def ShowFig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["Clap"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def Setup():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = RandomSetOfMean(100)
        mean_list.append(setOfMeans)
    ShowFig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of the sampling distribution is ", mean)

Setup()

def StDev():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = RandomSetOfMean(100)
        mean_list.append(setOfMeans)
    std = statistics.stdev(mean_list)
    print("Std of sampling distribution is ", std)

StDev()