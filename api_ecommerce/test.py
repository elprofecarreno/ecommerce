import unittest
from api.dao import dao
from test.dao.testdao import TestDAO

if __name__ == '__main__':
    # Crear una instancia de la clase TestDAO
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestDAO)
    
    # Crear el objeto TestRunner y ejecutar las pruebas
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)