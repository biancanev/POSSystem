# POSSystem

This is the documentation for our custom POS system

This is the current layout of our repository:
```
POSSystem/
┣ system/
┃ ┣ auth.py
┃ ┣ backend.py
┃ ┣ git_line.bat
┃ ┣ gui.py
┃ ┣ inventory.py
┃ ┗ user.py
```

### `auth.py`
Required files: `user.py`
Packages: `pymongo`, `bcrypt`

Methods:
| Name | Parameters | Return Value | Description |
| --- | --- | --- | --- |
| `authenticateUser` | `username - String`, `password - String` | `User (Object)` | Request user data from MongoDB. Compares hashed password data to authenticate user via bcrypt. If fields are correct, return the user object. Otherwise returns `None`.
