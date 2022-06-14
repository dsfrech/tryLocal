"""Use classes from user.py to have admin and user"""
from user import User
from user import Admin as AA

dsf = User('david','frech')
dsf.greeting()
dsf.describe_user()

# NOTICE: Admin class now refered as AA because of import as

dsf = AA("David", "Frech", ["can store","can delete"])
dsf.describe_user()
dsf.showprivileges()
dsf.addprivileges(['can update', 'is master'])
dsf.showprivileges()
