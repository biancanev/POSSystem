#ifndef BACKEND_H
#define BACKEND_H

#include <map>
#include <string>
#include <cmath>

using namespace std;

class Item{
    private:
        int id, upc, price;
        string name;
    protected:
    public:
    Item findItemById(int id){
        //TODO: connect to Mongodb to find item by id
    }
    Item findItemByUPC(int upc){
        //TODO: connect to Mongodb to find item by upc
    }
    Item findItemByName(string name){
        //TODO: connect to Mongodb to find item by name
    }
    bool IsValidItem(){
        if(id == -1){
            return false;
        }
        return true;
    }
};

class Cart{
    private:
        std::map<Item, int> cart_items;
    protected:

    public:
        Cart(){}
        std::map<Item, int> getCartContents(){
            return this->cart_items;
        }
        /**
         * Function: Add item to the cart. Verifies with a database that the item is a valid item
         * Inputs(overloaded):
         *      int id: id of the item to be searched for
         * Return:
         *      int status -
         *          0: item successfully added to cart
         *          -1: item is not a valid item
        **/
        int addItemtoCart(int num){
            Item newItem;
            if(int(log10(num)) + 1 == 12){
                newItem.findItemByUPC(num);
                if(newItem.IsValidItem()){
                    map<Item, int>::iterator it;
                    it = cart_items.find(newItem);
                    if(it == cart_items.end()){
                        cart_items.insert(pair<Item, int>(newItem, 1));
                    }else{
                        it->second++;
                    }
                    return 0;
                }else{
                    return -1;
                }
            }else{
                newItem.findItemById(num);
                if(newItem.IsValidItem()){
                    map<Item, int>::iterator it;
                    it = cart_items.find(newItem);
                    if(it == cart_items.end()){
                        cart_items.insert(pair<Item, int>(newItem, 1));
                    }else{
                        it->second++;
                    }
                    return 0;
                }else{
                    return -1;
                }
            }
        }

        int removeItemFromCart(int num){
            Item delItem;
            map<Item, int>::iterator it;
            it = cart_items.find(delItem);
        }
};
#endif