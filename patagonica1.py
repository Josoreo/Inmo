import pandas as pd
import math
from sendinbluedinamictemplate import send_email


df = pd.read_excel('Prueba.xlsx', header=None)

for i in range(2, len(df)):
    send_email(df[1][i], df[2][i], df[3][i])
