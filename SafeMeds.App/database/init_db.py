import mysql.connector

# Connect directly to your Aiven MySQL database
conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
    
)

cursor = conn.cursor()

# Create the inventory table
create_table_query = """
CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sku INT NOT NULL UNIQUE,
    category VARCHAR(100) NOT NULL,
    current_stock INT NOT NULL,
    reorder_point INT NOT NULL,
    last_restocked DATE NOT NULL,
    safety_rating VARCHAR(50) NOT NULL
);
"""

cursor.execute(create_table_query)
conn.commit()

print("Table 'inventory' created successfully in Aiven!")

cursor.close()
conn.close()



