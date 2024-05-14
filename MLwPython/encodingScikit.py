import pandas as pd
import plotnine as pn
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data_location= 'MLwPython\\tweets.csv'

pd.options.display.max_columns= 500

tweet_data= pd.read_csv(data_location)


# Divido los datos en train y test
train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)



# Standarizamos los datos
variables = ['language']
languages = ['en', 'es', 'au']

encoder = preprocessing.OneHotEncoder(categories=[languages], handle_unknown='ignore')
encoder.fit(train[variables])

print(encoder.categories_)
print(pd.DataFrame(encoder.transform(train[variables]).toarray()))
