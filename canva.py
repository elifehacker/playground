# role = "service_a"
# store = ParameterStore()
# foo_id = store.create_parameter(role, "someParamValue")
# store.get_parameter(role, foo_id) -> "someParamValue"

""" 
key -> val  service_a
k2-> v2    service_b

dictionary access 
key: roles
val: list[] access to id of the parameter pairs

dictionary stores
id: paramvalue 

"""

from typing import List, Iterable

# Any calls made to this parameter store are authenticated, assume role is valid.
class ParameterStore:

    def __init__(self):

        self.access = dict()
        self.parameters = dict()
        self.id_counter = 0
        self.granted_access = dict()

    def create_parameter(self, role: str, value: str) -> str:
        """Creates a parameter and returns the parameter id"""
        if role not in self.access:
            self.access[role] = list()
        self.access[role].append(self.id_counter)
        self.parameters[self.id_counter] = value

        self.id_counter += 1
        return self.id_counter - 1

    def get_parameter(self, role: str, parameter_id: str) -> str:
        """Returns the parameter value, if the role can access the parameter."""
        if role not in self.access.keys() and role not in self.granted_access.keys():
            raise Exception('role does not exist')
        if parameter_id not in self.access[role] and parameter_id not in self.granted_access[role]:
            raise Exception('do not have permission to '+parameter_id)
        if parameter_id not in self.parameters.keys():
            raise Exception('parameter_id '+parameter_id+' does not exist')
        return self.parameters[parameter_id]

    def get_parameter_ownership(self, role: str, parameter_id: str) -> str:
        """Returns the parameter value, if the role can access the parameter."""
        if role not in self.access.keys():
            raise Exception('role does not exist')
        if parameter_id not in self.access[role]:
            raise Exception('do not have permission to '+parameter_id)
        if parameter_id not in self.parameters.keys():
            raise Exception('parameter_id '+parameter_id+' does not exist')
        return self.parameters[parameter_id]

    def find_parameters(self, role: str) -> Iterable[str]:
        """Returns a list of parameter ids that the given role can access."""
        params = list()
        if role in self.access.keys():
            params = self.access[role]
        if role in self.granted_access.keys():
            params += self.granted_access[role]
        return params

    def share_parameter(self, role: str, parameter_id: str, role_to_share_with: str) -> None:
        """Share a parameter with a given role. Assume role ids are valid"""
        self.get_parameter_ownership(role, parameter_id)

        if role_to_share_with not in self.granted_access:
            self.granted_access[role_to_share_with] = list()
        self.granted_access[role_to_share_with].append(parameter_id)
        



