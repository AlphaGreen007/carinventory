import psycopg2

conn = psycopg2.connect("postgresql://car_parts:testing@localhost/car_parts")
cur = conn.cursor()

print("To demonstrate functionality of the SQL tables, this script automatically displays all fields from each of the three tables:")
 
SELECT * FROM manufacturers;
SELECT * FROM repairs;
SELECT * FORM prospective_customers;
