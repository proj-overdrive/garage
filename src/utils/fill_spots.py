import psycopg2
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Generate fake Spot data
def generate_spot_data():
    return {
        "owner_id": fake.uuid4(),
        "address": fake.address().replace("\n", ", "),
        "latitude": random.uniform(48.40, 48.45),
        "longitude": random.uniform(-123.40, -123.30)
    }

# Insert fake data into the 'spot' table
def insert_fake_data(conn, num_records):
    cursor = conn.cursor()
    
    for _ in range(num_records):
        spot = generate_spot_data()
        try:
            cursor.execute(
                """
                INSERT INTO spot (owner_id, address, latitude, longitude)
                VALUES (%s, %s, %s, %s);
                """,
                (spot['owner_id'], spot['address'], spot['latitude'], spot['longitude'])
            )
        except Exception as e:
            print(f"Error inserting data: {e}")
            conn.rollback()
            continue
    
    conn.commit()
    cursor.close()
    print(f"{num_records} records inserted successfully!")

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        insert_fake_data(conn, 100)  # Generate and insert 100 records
        conn.close()
