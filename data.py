
import pandas as pd
from pathlib import Path 

directory = (
    Path.home()
    /'Desktop'
    /'data'
)

file = directory / 'U.S._Chronic_Disease_Indicators__CDI_.csv'
usa_health = pd.read_csv(file)

# delete all columns with no data
usa_health.dropna(axis=1, how='all', inplace=True)
# get all columns in lowercase and for those columns that have 'ID' separate ID from main title with _
usa_health.columns = ['_ID'.join(col.split('ID')).lower() for col in usa_health.columns]

def usa_health_data(usa: pd.DataFrame) -> pd.DataFrame:

    '''get dataframe for export'''
    return usa 

usa_data = usa_health_data(usa_health)