const { default: mongoose } = require("mongoose");
const Mongoose = require("mongoose");
const ItemSchema = new Mongoose.Schema({
    upc: {
        type: Number,
        unique: true,
        required
    },
    id: {
        type: Number,
        unique: true,
        required
    },
    name: {
        type: String,
    },
    quantity: {
        type: Number,
        required
    }
});

const Item = Mongoose.model("item", ItemSchema);
module.exports = Item;