import unittest
from api.dao import dao

class TestDAO(unittest.TestCase):

    def test_statement_select_all(self):
        table_name = 'depots'
        columns_name = ['depot_id', 'depot_name', 'depot_location']
        expected = 'SELECT depot_id, depot_name, depot_location FROM depots'
        result = dao.statement_select_all(table_name, columns_name)
        self.assertEqual(result, expected)

    def test_statement_select_by_id(self):
        table_name = 'depots'
        columns_name = ['depot_id', 'depot_name', 'depot_location']
        expected = 'SELECT depot_id, depot_name, depot_location FROM depots WHERE depot_id = %s'
        result = dao.statement_select_by_id(table_name, columns_name)
        self.assertEqual(result, expected)

    def test_statement_insert_autoincrement_id(self):
        table_name = 'depots'
        columns_name = ['depot_id', 'depot_name', 'depot_location']
        expected = 'INSERT INTO depots (depot_name, depot_location) VALUES (%s, %s)'
        result = dao.statement_insert_autoincrement_id(table_name, columns_name)
        self.assertEqual(result, expected)

    def test_statement_update_by_id(self):
        table_name = 'depots'
        columns_name = ['depot_id', 'depot_name', 'depot_location']
        expected = 'UPDATE depots SET depot_name = %s, depot_location = %s WHERE depot_id = %s'
        result = dao.statement_update_by_id(table_name, columns_name)
        self.assertEqual(result, expected)

    def test_statement_delete_by_id(self):
        table_name = 'depots'
        columns_name = ['depot_id', 'depot_name', 'depot_location']
        expected = 'DELETE FROM depots WHERE depot_id = %s'
        result = dao.statement_delete_by_id(table_name, columns_name)
        self.assertEqual(result, expected)