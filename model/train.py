import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import argparse
import os

parser = argparse.ArgumentParser() #sets up the framework for accepting command-line arguments when the script is executed
parser.add_argument("--input_data", type=str, help="") # 
parser.add_argument("--output_model", type=str ,help="") #
args= parser.parse_args() #Parsing the Actual input

print("Reading input data")
df = pd.read_csv(args.input_data)#Reading input data 

df.replace({"YES": 1, "NO:":0 "M": 1, "F":0}, inplace=True)

if "LUNG_CANCER" in df.columns:
    raise ValueError("Target comlumn LABEL not found after preprocessing")

x =df.drop(labels)
