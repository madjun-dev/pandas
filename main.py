import pandas as pd

outlook = [
    "sunny","sunny","overcast","rainy","rainy",
    "rainy","overcast","sunny","sunny","rainy",
    "sunny","overcast","overcast","rainy"
]
temp = [
    "hot","hot","hot","mild","cool",
    "cool","cool","mild","cool","mild",
    "mild","mild","hot","mild"
]
humidity = [
    "high","high","high","high","normal",
    "normal","normal","high","normal","normal",
    "normal","high","normal","high",
]
windy = [
    False,True,False,False,False,
    True,True,False,False,False,
    True,True,False,True
]

play = [
    "no","no","yes","yes","yes",
    "no","yes","no","yes","yes",
    "yes","yes","yes","no"
]

df = pd.DataFrame(
    {
        "outlook" :outlook,
        "temp" : temp,
        "humidity" : humidity,
        "windy" : windy,
        "play" : play
    }
)
print('--------------')
print(df)
print('--------------')
print(df.shape)
print('--------------')
print(df.describe())
print('--------------')
print(df.outlook.describe())
print('--------------')
df["new column"]= "new value"
print(df)
df["play-1"]=df["play"].shift(-1)
print(df)
print(df.head())
print(df.head(7))
print(df.tail())
print(df.tail(7))
print(df.sample())
print(df[["outlook","play"]])
print(df.outlook)
print(df.outlook.unique())
