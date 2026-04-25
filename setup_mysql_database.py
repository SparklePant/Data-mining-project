"""
This script creates a MySQL database and loads the data from Excel.
You should run it once you have MySQL installed and configured.
If you want to use avoid changing anything, I recommend making your MySQL root password "root123".
"""

import pandas as pd
import mysql.connector
from mysql.connector import Error
import warnings
warnings.filterwarnings('ignore')

def create_database_connection(host='localhost', user='root', password='your_password'):
    """Create a connection to MySQL server"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(connection, db_name='telco_churn_db'):
    """Create database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")

def load_data_to_mysql(excel_file, host='localhost', user='root', password='your_password', 
                       db_name='telco_churn_db', table_name='customer_churn'):
    """Load data from Excel to MySQL"""
    
    # Read Excel file
    print("Reading Excel file...")
    df = pd.read_excel(excel_file)
    df.columns = df.columns.str.strip()
    print(f"Loaded {len(df)} rows with {len(df.columns)} columns")
    
    # Create connection
    connection = create_database_connection(host, user, password)
    if not connection:
        return
    
    # Create database
    create_database(connection, db_name)
    connection.close()
    
    # Connect to the new database
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        
        cursor = connection.cursor()
        
        # Create table with appropriate data types
        create_table_query = f"""
        CREATE TABLE {table_name} (
            CustomerID VARCHAR(50) PRIMARY KEY,
            Count INT,
            Country VARCHAR(50),
            State VARCHAR(50),
            City VARCHAR(100),
            Zip_Code VARCHAR(20),
            Lat_Long VARCHAR(100),
            Latitude DECIMAL(10, 6),
            Longitude DECIMAL(10, 6),
            Gender VARCHAR(10),
            Senior_Citizen VARCHAR(5),
            Partner VARCHAR(5),
            Dependents VARCHAR(5),
            Tenure_Months INT,
            Phone_Service VARCHAR(5),
            Multiple_Lines VARCHAR(50),
            Internet_Service VARCHAR(50),
            Online_Security VARCHAR(50),
            Online_Backup VARCHAR(50),
            Device_Protection VARCHAR(50),
            Tech_Support VARCHAR(50),
            Streaming_TV VARCHAR(50),
            Streaming_Movies VARCHAR(50),
            Contract VARCHAR(50),
            Paperless_Billing VARCHAR(5),
            Payment_Method VARCHAR(50),
            Monthly_Charges DECIMAL(10, 2),
            Total_Charges VARCHAR(20),
            Churn_Label VARCHAR(5),
            Churn_Value INT,
            Churn_Score INT,
            CLTV INT,
            Churn_Reason VARCHAR(200)
        )
        """
        
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully")
        
        # Prepare insert query
        columns = ', '.join([col.replace(' ', '_') for col in df.columns])
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        
        # Replace pandas NaN values with None so MySQL stores them as NULL
        df = df.where(pd.notnull(df), None)
        
        # Insert data
        print("Inserting data into MySQL...")
        for idx, row in df.iterrows():
            values = [None if pd.isna(x) else x for x in row]
            cursor.execute(insert_query, tuple(values))
            if (idx + 1) % 1000 == 0:
                print(f"Inserted {idx + 1} rows...")
        
        connection.commit()
        print(f"Successfully loaded {len(df)} rows into MySQL table '{table_name}'")
        
        # Verify the data
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Verification: Table contains {count} rows")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"Error loading data to MySQL: {e}")

if __name__ == "__main__":
    # Configuration
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root123'  # Update this if you have a different password
    DATABASE_NAME = 'telco_churn_db'
    TABLE_NAME = 'customer_churn'
    EXCEL_FILE = 'Telco_customer_churn.xlsx'
    
    print("="*60)
    print("MySQL Database Setup for Telco Customer Churn")
    print("="*60)
    
    load_data_to_mysql(
        excel_file=EXCEL_FILE,
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db_name=DATABASE_NAME,
        table_name=TABLE_NAME
    )
    
    print("\nSetup complete!")
    print(f"Database: {DATABASE_NAME}")
    print(f"Table: {TABLE_NAME}")