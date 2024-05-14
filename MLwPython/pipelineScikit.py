from sklearn.compose import ColumnTransformer
import plotnine as pn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd



# Selecciono los datos
data_location= 'MLwPython\\tweets.csv'

pd.options.display.max_columns= 500

tweet_data= pd.read_csv(data_location)


# Divido los datos en train y test
train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)


# Creo una pipeline con los datos numéricos (con una función de scaler, para estandarizarlos)
numeric_variables = ['number_of_likes', 'number_of_shares']
numeric_pipeline = Pipeline(
    [
        ('scaler', StandardScaler())
    ]
)

# Creo una pipeline con los idiomas, con una función de enconder para convertir los datos no numéricos en valores de 0 y 1, y selecciono es y en solo 
categoric_variables = ['language']
languages = ['en', 'es']
categoric_pipeline = Pipeline(
    [
        ('encoder', OneHotEncoder(categories=[languages], handle_unknown='ignore'))
    ]
)

# Junto los pipelines
preprocessing = ColumnTransformer(
    [
        ('numeric', numeric_pipeline, numeric_variables),
        ('categorical', categoric_pipeline, categoric_variables)
    ]
)

# Completo el pipeline total uniendo la regresión
full_pipeline = Pipeline(
    [
        ('preprocessing', preprocessing),
        ('regression', LinearRegression())
    ]
)



X_variables = numeric_variables + categoric_variables
y_variable = 'number_of_likes'

full_pipeline.fit(train[X_variables], train[y_variable])

test['prediction'] = full_pipeline.predict(test[X_variables])

graph = (
    pn.ggplot(test, pn.aes(x='number_of_likes', y='prediction')) 
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

print(train[y_variable])
