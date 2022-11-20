import pandas as pd
import numpy as np

def getRandomProducts(num=10):
    df = pd.read_excel("static/dataset.xlsx")
    df_ids = df["Id"].copy()
    df_ids = df_ids.to_numpy()
    np.random.shuffle(df_ids)
    randProducts = df_ids.tolist()

    prodCost = []
    for i in range(0, len(randProducts)):
        prodCost.append(df["Amount"][df["Id"] == df_ids[i]].to_list()[0])

    prodType = []
    for i in range(0, len(df_ids)):
        prodType.append(df["ProductType"][df["Id"] == df_ids[i]].to_list()[0])

    prodName = []
    for i in range(0, len(df_ids)):
        prodName.append(df["Name"][df["Id"] == df_ids[i]].to_list()[0])


    return randProducts, prodCost, prodType, prodName


def getProductInfo(id):
    df = pd.read_excel("static/dataset.xlsx")
    prodCost = df["Amount"][df["Id"] == id].to_list()[0]
    prodType = df["ProductType"][df["Id"] == id].to_list()[0]
    prodName = df["Name"][df["Id"] == id].to_list()[0]
    prodDesc = df["Description"][df["Id"] == id].to_list()[0].split("\n")
    prodDescLen = len(prodDesc)
    return prodCost, prodType, prodName, prodDesc, prodDescLen