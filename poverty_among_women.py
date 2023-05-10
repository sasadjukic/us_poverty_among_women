
import pandas as pd 
from data import usa_data 

def get_poverty_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    '''get the right survey question'''
    poverty = data[data['question'] == 'Poverty among women aged 18-44 years']
    return poverty 

def get_us_states_only(data: pd.DataFrame) -> pd.DataFrame:
    '''get only 50 US states + DC'''
    states = data.loc[
                        (data['locationdesc'] != 'United States') &
                        (data['locationdesc'] != 'Puerto Rico') &
                        (data['locationdesc'] != 'Guam') &
                        (data['locationdesc'] != 'Virgin Islands')
                    ]

    return states

def get_poverty_for_2019(poverty: pd.DataFrame) -> pd.DataFrame:
    '''get poverty data for 2019 (the last year with info)'''
    p_2019 = poverty[poverty['yearstart'] == 2019]
    return p_2019

poverty = get_poverty_dataframe(usa_data)
states = get_us_states_only(poverty)
poverty_2019 = get_poverty_for_2019(states)
nationwide = poverty_2019[['yearstart', 'locationabbr', 'datavaluealt']]