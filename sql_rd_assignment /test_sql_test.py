import unittest

import sqlite3

from sql_test import DatabaseEditor


class TestSqlData(unittest.TestCase):
    def setUp(self):
        self.new_output = DatabaseEditor()
        self.new_output.db = sqlite3.connect(":memory:")
        self.new_output.c = self.new_output.db.cursor()

        self.new_output.c.execute("CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, created "
                                  "timestamp with time zone NOT NULL, modified timestamp with time zone NOT NULL, "
                                  "description character varying(255) NOT NULL, amount numeric(12,2) NOT NULL); ")

    def read_data(self):
        self.new_output.adding_additional_column()
        self.new_output.data_entry()

    def query_data(self):
        self.new_output.c.execute("SELECT count(*) FROM products")
        result = self.new_output.c.fetchone()[0]
        print(result)
        return result

    def test_number_rows(self):
        self.read_data()
        self.assertEqual(self.query_data(), 20)

    def tearDown(self):
        self.new_output.db.close()


if __name__ == "__main__":
    unittest.main()
