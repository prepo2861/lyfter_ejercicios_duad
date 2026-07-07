"""
Cree una clase abstracta User con los siguientes métodos abstractos:
get_role()
has_permission(permission)
Luego cree dos clases que hereden de ella:
AdminUser
RegularUser
Cada una debe implementar los métodos
Por ejemplo:
AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)

"""

from abc import ABC, abstractmethod


class User(ABC):

    # Constructor used to initialize the user's name
    def __init__(self, name):
        self.name = name

    # Abstract method that returns the user's role
    @abstractmethod
    def get_role(self):
        pass

    # Abstract method that checks if the user has a permission
    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):

    # AdminUser inherits the name from User
    def __init__(self, name):
        super().__init__(name)

    # Return the admin role
    def get_role(self):
        return "Admin"

    # Admin users have all permissions
    def has_permission(self, permission):
        return True


class RegularUser(User):

    # RegularUser inherits the name from User
    def __init__(self, name):
        super().__init__(name)

    # Return the regular user role
    def get_role(self):
        return "Regular User"

    # Regular users only have read permission
    def has_permission(self, permission):
        permission = permission.lower()

        if permission == "read":
            return True

        return False
        

