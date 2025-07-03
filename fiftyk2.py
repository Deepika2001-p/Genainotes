
import pandas as pd
from sqlalchemy import create_engine

# Load your CSV
df = pd.read_csv('dirty_education_data_50k.csv')

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:Deepika%40464@localhost/educationdetails_db")

# Save to MySQL
df.to_sql(name='education_details', con=engine, if_exists='replace', index=False)

print("✅ Data saved to MySQL using SQLAlchemy!")

