import unittest
from canva import ParameterStore


class ParameterStoreTest(unittest.TestCase):

    role1 = "ROLE_1"
    role2 = "ROLE_2"

    def setUp(self):
       self.store = ParameterStore()

    def test_create(self):
       param_id = self.store.create_parameter(self.role1, "Some Value")
       retrieved_value = self.store.get_parameter(self.role1, param_id)
       self.assertEqual("Some Value", retrieved_value)

       # Should not have access - What should happen here?
       with self.assertRaises(Exception):
           self.store.get_parameter(self.role2, param_id)

    def test_sharing(self):
       # self, role: str, parameter_id: str, role_to_share_with: str
       param_id = self.store.create_parameter(self.role1, "Some Value")
       self.store.share_parameter(self.role1, param_id, self.role2)
       l = self.store.find_parameters(self.role2)
       self.assertEqual([param_id], l)

    def test_sharing_to_fail(self):
        with self.assertRaises(Exception):
           param_id = self.store.create_parameter(self.role1, "Some Value")
           self.store.share_parameter(self.role1, param_id+1, self.role2)
        
if __name__ == '__main__':
    unittest.main()
