import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
#import openpyxl
df = pd.read_excel(
    "C:/Users/Pavani/OneDrive/Attachments/Desktop/COVID19ANANALYSIS/covid.xlsx")
#pd.set_option("display.max_rows", None)
print(df)
df=df.rename(columns={"TotÂ\xa0Cases//1M pop":"toal_cases//1M","TotÂ\xa0Deaths/1M pop":'toal_deaths//1M'})
print(df)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.dtypes)
print(df.info())
print(df.columns)
print(df.isnull().sum())
# Fill missing numerical values with mean
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical missing values
cat_cols = df.select_dtypes(include='object').columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# Remove duplicates
df.drop_duplicates(inplace=True)
# Remove duplicates
print(df.drop_duplicates(inplace=True))
print(df['Country'].value_counts().sum())
print(df['Other names'].value_counts().sum())
print(df["ISO 3166-1 alpha-3 CODE"].value_counts().sum())
print(df['Population'].describe())
print(df['Continent'].value_counts())
print(df['Total Cases'].describe())
print(df['Total Deaths'].describe())
print(df['toal_cases//1M'].describe())
print(df['toal_deaths//1M'].describe())
print(df['Death percentage'].describe())
continuous=[ 'Population', 'Total Cases', 'Total Deaths', 'toal_cases//1M',
       'toal_deaths//1M', 'Death percentage']
print(df[continuous].describe())
print(df[continuous].skew())
categorical=['Country', 'Other names','Continent']
print(df[categorical].nunique())
#print(df[categorical].value_counts())
print(df['Continent'].value_counts())
print(df['Continent'].unique())
sns.histplot(df["Population"],bins=10,kde=True)
plt.show()
print(sns.boxplot(x=df["Population"]))
plt.show()
print(sns.kdeplot(df["Population"]))
plt.show()
print(sns.histplot(df['Total Cases'],bins=10,kde=True))
plt.show()
print(sns.boxplot(x=df['Total Cases']))
plt.show()
print(sns.kdeplot(df['Total Cases']))
plt.show()
print(sns.histplot(df['Total Deaths'],bins=10,kde=True))
plt.show()
print(sns.boxplot(x=df['Total Deaths']))
plt.show()
print(sns.kdeplot(df['Total Deaths']))
plt.show()
print(sns.histplot(df['toal_cases//1M'],bins=10,kde=True))
plt.show()
print(sns.boxplot(x=df['toal_cases//1M']))
plt.show()
print(sns.kdeplot(df['toal_cases//1M']))
plt.show()
print(sns.histplot(df[ 'toal_deaths//1M'],bins=10,kde=True))
plt.show()
print(sns.boxplot(x=df['toal_deaths//1M']))
plt.show()
print(sns.kdeplot(df[ 'toal_deaths//1M']))
plt.show()
print(sns.histplot(df['Death percentage'],bins=10,kde=True))
plt.show()
print(sns.boxplot(x=df['Death percentage']))
plt.show()
print(sns.kdeplot(df['Death percentage']))
plt.show()
df.hist(figsize=(12,8))
plt.title("OverAll Observations")
plt.show()
plt.pie(x=df["Continent"].value_counts(),labels=df["Continent"].value_counts().index,autopct="%0.1f%%",explode=[0,0.05,0.05,0,0,0])
plt.show()
print(sns.countplot(x=df["Continent"]))
country_summary = df.groupby('Country').agg({
    'Population'  : 'sum',
    'Total Cases' : 'sum',
    'Total Deaths': 'sum',
}).sort_values(by='Total Cases', ascending=False)
print(country_summary.head(10))
plt.scatter(df["Total Cases"], df["Total Deaths"])
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.title("Confirmed vs Deaths")
plt.show()
top10 = df.groupby('Country')['Total Cases'].sum().sort_values(ascending=False).head(10)
top10.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 Countries by Confirmed Cases")
plt.ylabel("Cases")
plt.show()
plt.bar(df["Continent"],df['Death percentage'],width=0.5,label=df['Continent'])
plt.show()
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
