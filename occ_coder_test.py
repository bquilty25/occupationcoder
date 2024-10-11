import pandas as pd
from occupationcoder.coder import coder
myCoder = coder.Coder()

if __name__ == '__main__':
   df = pd.read_csv("occupationcoder/testvacancies/test_vacancies.csv", encoding='latin-1')
   df = myCoder.codedataframe(df)
   
   # Display the first few rows of the DataFrame
print(df)