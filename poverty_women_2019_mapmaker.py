

# import libraries and modules
import pandas as pd 
import plotly.express as px 
from poverty_among_women import nationwide 

def display_poverty_among_women_map(nation: pd.DataFrame) -> None:
    '''display USA map with states colored to match their percentage of women living in poverty'''

    fig = px.choropleth(
                        nation, 
                        locations='locationabbr',
                        locationmode='USA-states',
                        scope='usa',
                        color='datavaluealt',
                        range_color=[0, 45],
                        color_continuous_scale=['#ffffff', '#fdfdde', '#ece3b4', '#e9d28d', '#d7b54f', '#c88a31', '#925806']
          ).update_layout(
                        template='none',
                        plot_bgcolor='#2C3333',
                        paper_bgcolor = '#2C3333'
          )

    fig.show()

display_poverty_among_women_map(nationwide)
