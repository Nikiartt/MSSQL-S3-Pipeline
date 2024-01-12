from Connection_MsSQL import cursor,conn   
import pandas as pd

cursor.execute("""DELETE FROM Covid WHERE Country='Afghanistan'; """)

conn.commit()