#ifndef BACKEND_H
#define BACKEND_H

#include <map>
#include <string>
#include <cmath>

using namespace std;

class Item{
        int id, upc, price;
        string name;

    protected:
    public:
        void findItemById(int id){
            //TODO: connect to Mongodb to find item by id
        }
        void findItemByUPC(int upc){
            //TODO: connect to Mongodb to find item by upc
        }
        void findItemByName(string name){
            //TODO: connect to Mongodb to find item by name
        }
        bool isValidItem(){ return id == -1 ? false : true; }
};

class Cart{
    protected:
        std::map<Item, int> cartItems;
        double subtotal, tax, total;
    public:
        Cart();
        std::map<Item, int> getCartContents(){ return this->cartItems; }
        int addItemToCart(int); // item number
        int removeItemFromCart(int); // item number
};

Cart::Cart()
    : subtotal(0), tax(0), total(0) {}

/**
 * Function: Adds item to the cart. Verifies with a database that the item is a valid item
 * Inputs(overloaded):
 *      int id: id of the item to be searched for
 * Return:
 *      int status -
 *          0: item successfully added to cart
 *          -1: item is not a valid item
**/
int Cart::addItemToCart(int num){
    Item newItem;
    if(int(log10(num)) + 1 == 12){
        newItem.findItemByUPC(num);
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

#endif