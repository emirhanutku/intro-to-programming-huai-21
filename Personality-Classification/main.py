import pandas as pd
df=pd.read_csv("16P.csv",encoding="ISO-8859-1")
df1=df.drop(["Response Id"], axis=1)
df.drop(["Response Id"],inplace=True, axis=1)


personality_encode={"ESTJ":0,"ENTJ":1 , "ESFJ":2, "ENFJ":3, "ISTJ":4, "ISFJ":5, "INTJ":6, "INFJ":7, "ESTP":8 , "ESFP":9, "ENTP":10, "ENFP":11, "ISTP":12, "ISFP":13, "INTP":14,"INFP":15}
for i in ("ESTJ", "ENTJ", "ESFJ", "ENFJ", "ISTJ", "ISFJ", "INTJ", "INFJ", "ESTP" , "ESFP", "ENTP", "ENFP", "ISTP", "ISFP", "INTP","INFP"):
    df.replace(to_replace=i ,value=personality_encode[i],inplace=True)
    df1.replace(to_replace=i, value=personality_encode[i], inplace=True)

for k in range(len(df)):
    for i in list(df.columns):
        if i=="Personality":
            break
        else:
            df1.loc[k,[i]]=(df1.loc[k,[i]]-(-3))/6
print(df1.head(12))
