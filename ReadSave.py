import pandas as pd
from Connection_MsSQL import conn   
distinct_countries_query = "SELECT DISTINCT Country AS [Distinct Countries] FROM Covid;"
distinct_countries_df = pd.read_sql(distinct_countries_query, conn)
# for i in range(len(distinct_countries_df)):
for i in range(3):
    country_name=distinct_countries_df.loc[i,'Distinct Countries']
    country_query=f"SELECT * FROM Covid WHERE Country='{country_name}' ORDER BY Date_reported ASC;"
    country_df= pd.read_sql(country_query, conn)
    country_df.to_csv(f'data/to_S3/{country_name}.csv',index=False)
    print(country_df)



    