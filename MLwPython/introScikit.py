import pandas as pd
import plotnine as pn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

data_location= 'MLwPython\\tweets.csv'

pd.options.display.max_columns= 500

tweet_data= pd.read_csv(data_location)

print(tweet_data.shape)

print(tweet_data.head)

    
X_variables = ['number_of_shares']
y_variable = 'number_of_likes'
model = LinearRegression()
model.fit(tweet_data[X_variables], tweet_data[y_variable])
tweet_data['predictions_lin_reg'] = model.predict(tweet_data[X_variables])
model = DecisionTreeRegressor(random_state=0)
model.fit(tweet_data[X_variables], tweet_data[y_variable])
tweet_data['predictions_dt_reg'] = model.predict(tweet_data[X_variables])
# Creamos un grafico simple para visualizar
columns = [y_variable, 'predictions_lin_reg', 'predictions_dt_reg']
graph_data = pd.melt(tweet_data[columns], y_variable)
graph = (
    pn.ggplot(graph_data, pn.aes(x='number_of_likes', y='value', color='variable')) 
    + pn.geom_point(alpha=0.4)
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
    + pn.ylab('prediction')

)

graph.show()
graph.save()