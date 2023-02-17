# import plotly.express as px
# data_all = px.data.gapminder()

# data = data_all[data_all.country == 'China']
# fig = px.bar(
#   data,
#   x='year',
#   y='pop',
#   hover_data=['lifeExp', 'gdpPercap'],
#   color='lifeExp',
#   labels={
#     'pop': 'population of China' 
#   },
#   height=400
# )
# fig.show()

import plotly.graph_objects as go
animals = ['giraffes', 'orangutans', 'monkeys']
 
fig = go.Figure(data=[
    go.Scatter(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Scatter(name='LA Zoo', x=animals, y=[12, 18, 29])
])
fig.show()
