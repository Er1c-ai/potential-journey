import psycopg2

import datetime

import time

import random

import csv

import argparse

DBNAME = "rd_assignment"


class DatabaseEditor(object):
    def __init__(self):
        self.db = psycopg2.connect(database=DBNAME)
        self.c = self.db.cursor()

    def adding_additional_column(self):
        query = "ALTER TABLE products ADD is_active boolean"
        self.c.execute(query)
        self.db.commit()

    def data_entry(self):
        for i in range(20):
            description = time.time()
            created = str(datetime.datetime.fromtimestamp(description).strftime("%Y-%m-%d %H:%M:%S "))
            modified = str(datetime.datetime.fromtimestamp(description).strftime("%Y-%m-%d %H:%M:%S "))
            amount = random.randrange(0, 1000)
            is_active = random.choice(['True', 'False'])
            self.c.execute(
                f"""INSERT INTO products(created, modified, description, amount, is_active) VALUES ('{created}', '{modified}', '{description}' ,
                                       '{amount}' ,'{is_active}')""")
            self.db.commit()


    def read_data_from_database(self):
        self.c.execute("SELECT * FROM products")
        rows = self.c.fetchall()
        self.write_to_csv(rows)

    def highest_amount_table_data(self, output_file):
        self.c.execute("SELECT * FROM products ORDER BY amount DESC")
        rows = self.c.fetchall()
        self.write_to_csv(rows, output_file)

    def active_products_amount_above_10(self, output_file):
        self.c.execute("SELECT * FROM products WHERE is_active = TRUE AND amount > 10")
        rows = self.c.fetchall()
        self.write_to_csv(rows, output_file)

    def inactive_products_eluding_certain_fields(self, output_file):
        self.c.execute("SELECT is_active, description, amount FROM products WHERE is_active = FALSE")
        rows = self.c.fetchall()
        self.write_to_csv(rows, output_file)

    def write_to_csv(self, lines, output_csv):
        with open(output_csv, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(lines)


if __name__ == "__main__":
    database_editor = DatabaseEditor()
    database_editor.adding_additional_column()
    database_editor.data_entry()
    parser = argparse.ArgumentParser(description="reading file")
    parser.add_argument('-o1', 'output_csv_file', help="writing file to another output")
    parser.add_argument('-o2', 'output2_csv_file', help="writing file to another output")
    parser.add_argument('-o3', 'output3_csv_file', help="writing file to another output")
    args = parser.parse_args()
    database_editor.highest_amount_table_data(args.output_csv_file)
    database_editor.active_products_amount_above_10(args.output2_csv_file)
    database_editor.inactive_products_eluding_certain_fields(args.output3_csv_file)
