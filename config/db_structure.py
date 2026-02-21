#IMPORTS HERE
from root import PROJECT_ROOT,ChangeRoot
import os

#INSTANCE STRUCTURE OF DB
class db_structure:
    instance = os.path.join(PROJECT_ROOT,'instance')
    instance_admin = os.path.join(instance,'admin')
    instance_user = os.path.join(instance,'user')
    instance_admin_employee = os.path.join(instance_admin,'employees')
    instance_admin_customer = os.path.join(instance_admin,'customer')
    
    def __init__(self):
        os.chdir(PROJECT_ROOT)
        os.makedirs(self.instance, exist_ok=True)
        os.makedirs(self.instance_admin, exist_ok=True)
        os.makedirs(self.instance_user, exist_ok=True)
        os.makedirs(self.instance_admin_employee, exist_ok=True)
        os.makedirs(self.instance_admin_customer, exist_ok=True)
      


