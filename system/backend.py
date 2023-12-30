import math as m

class Item:
    id = -1
    upc = 0
    price = 0
    name = ""
    
    def __init__(self, id, upc, price, name):
        self.id = id
        self.upc = upc
        self.price = price
        self.name = name
    
    def findItemById(id):
        #TODO: connect to Mongodb to find item by id
        pass
    def findItemByUPC(upc):
        #TODO: connect to Mongodb to find item by upc
        pass
    def findItemByName(name):
        #TODO: connect to Mongodb to find item by name
        pass
    def isValidItem(): return False if id == -1 else True

class Cart:
    cartItems = dict()
    subtotal = 0
    tax = 0
    total = 0
    def __init__(self, cartItems, subtotal, tax, total):
        self.cartItems = cartItems
        self.subtotal = subtotal
        self.tax = tax
        self.total = total
    def addItemToCart(self, num):
        if m.log10(num) + 1 == 12:
            Item.findItemByUPC(num)
            if Item.isValidItem():
                map<Item, int>::iterator it;
                it = cartItems.find(newItem);
                if it == cartItems.end() {
                    cartItems.insert(pair<Item, int>(newItem, 1));
                }else{
                    it->second++;
                }
                return 0;
            }
        }else{
            newItem.findItemById(num);
            if(newItem.isValidItem()){
                map<Item, int>::iterator it;
                it = cartItems.find(newItem);
                if(it == cartItems.end()){
                    cartItems.insert(pair<Item, int>(newItem, 1));
                }else{
                    it->second++;
                }
                return 0;
            }
        }
        return -1;
}

int Cart::removeItemFromCart(int num){
    Item delItem;
    map<Item, int>::iterator it;
    it = cartItems.find(delItem);
}

class Order : public Cart{
        int orderNumber;
        string orderName;
        
    public:
        Order(int, string); // order number, order name
        int getOrderNumber(){ return orderNumber; };
        void findOrderByUPC();
};

Order::Order(int num, string name)
    : Cart(), orderNumber(num), orderName(name) {}
