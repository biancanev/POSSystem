# POSSystem

This is the documentation for our custom POS system

This is the current layout of our repository:
```
POSSystem/
┣ system/
┃ ┣ auth.py
┃ ┣ backend.py
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
| `authenticateUser` | `username (str)`, `password (str)` | `User (Object)` | Request user data from MongoDB. Compares hashed password data to authenticate user via bcrypt. If fields are correct, return the user object. Otherwise returns `None`.

### `backend.py`
Required files: `auth.py`, `backend.py`, `user.py`
Packages: `pymongo`, `dotenv`, `os`

#### Objects:

`Item` - Object to contain item information

Variables:
| Name | Type | Description |
| --- | --- | --- |
| `id` | `int` | 6-digit item id. Similar to item SKU. |
| `upc` | `int` | 12-digit item id. Works universally with item barcodes. |
| `price` | `int` | Price of the item. |
| `name` | `str` | Name of the item. |
| `quantity` | `int` | Database value of item quantity |

Methods:
| Name | Parameters | Return Value | Description |
| --- | --- | --- | --- |
| `Item.__init__` | `None` | `None` | Default constructor |
| `Item.findItemById` | `id (int)` | `None` | Searches MongoDB for document that has the parameter `id`. Sets instance variables to recieved data. If MongoDB returns no data, `id` is set to -1 and all other instance variables are not instantiated.|
| `Item.findItemByUPC` | `upc (int)` | `None` | Searches MongoDB for document that has the parameter `upc`. Sets instance variables to recieved data. If MongoDB returns no data, `id` is set to -1 and all other instance variables are not instantiated.|
| `Item.findItemByName` | `name (str)` | `None` | Searches MongoDB for document that has the parameter `name`. Sets instance variables to recieved data. If MongoDB returns no data, `id` is set to -1 and all other instance variables are not instantiated.|
| `Item.isValidItem` | `None` | `bool` | Checks `id` instance variable. If `id` is -1, returns `False`, otherwise returns `True` |
| `Item.saveItemToDB` | `None` | `None` | Saves all instance variables into dictionary form and sends it to MongoDB. |
| `Item.addItemToDB` | `quantity (int)` | `None` | If MongoDB already has a document containing an item id with the same value as the instance vairalbe `self.id`, updates the document by adding `quantity` to stored value. Otherwise, calls `saveItemToDB` with `self.quantity` equal to the parameter `quantity` |

`Cart` - Object to contain cart information

Variables:
| Name | Type | Description |
| --- | --- | --- |
| `subtotal` | `int` | Subtotal of all items in cart |
| `tax` | `int` | Defined tax rate. |
| `total` | `int` | Total cost of items in cart, including tax |
| `items` | `list` | List of `Item` objects that are contained in the cart. |

Methods:
| Name | Parameters | Return Value | Description |
| --- | --- | --- | --- |
| `Cart.__init__` | `None` | `None` | Default constructor |
| `Cart.addItemToCart` | `num (int)` | `None` | Determines whether `num` is an id or UPC based on length. Searches for item information using `Item.findItemByID` or `Item.findItemByUPC`. Checks if item exists using `Item.isValidItem`. If item exists, appends item to `items` instance variable|