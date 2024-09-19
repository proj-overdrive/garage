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
        "id": fake.uuid4(),
        "owner_id": fake.uuid4(),
        "address": fake.address().replace("\n", ", "),
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180, 180),
    }

# Insert fake data into the 'spot' table
def insert_fake_data(conn, num_records):
    cursor = conn.cursor()
    
    for _ in range(num_records):
        spot = generate_spot_data()
        try:
            cursor.execute(
                """
                INSERT INTO spot (id, owner_id, address, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s);
                """,
                (spot['id'], spot['owner_id'], spot['address'], spot['latitude'], spot['longitude'])
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
