from Connection_MsSQL import cursor,conn
import pandas as pd

df_all=pd.read_csv('data\WHO-COVID-19-global-data.csv')
df_all['Country'] = df_all['Country'].str.replace(r"'", " ")
df_all['WHO_region'] = df_all['WHO_region'].str.replace(r"'", " ")
for i in range(len(df_all)):
    try:
        df_row=df_all.iloc[i]
        cursor.execute(f'''
                        INSERT INTO Covid (
                        Date_reported,
                        Country_code,
                        Country,
                        WHO_region,
                        New_cases,
                        Cumulative_cases,
                        New_deaths,
                        Cumulative_deaths)
                    
                        VALUES
                        ('{df_row['Date_reported']}',
                        '{df_row['Country_code']}',
                        '{df_row['Country']}',
                        '{df_row['WHO_region']}',
                        {df_row['New_cases']},
                        {df_row['Cumulative_cases']},
                        {df_row['New_deaths']},
                        {df_row['Cumulative_deaths']});
                        ''')
        conn.commit()
    except Exception as e :
        print(f'error in {i}',e) 
