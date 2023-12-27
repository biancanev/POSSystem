const { default: mongoose } = require("mongoose")
const Mongoose = require("mongoose")
const PCSchema = new Mongoose.Schema({
    cpu:{
        type: String,
        required: true
    },
    cooler:{
        type: String,
        required: true
    },
    motherboard:{
        type: String,
        required: true
    },
    ram:{
        type: String,
        required: true
    },
    gpu:{
        type: String,
    },
    pccase:{
        type: String,
        required: true
    },
    cooling:{
        type: String,
    },
    os:{
        type: String,
        required: true
    },
    associatedID:{
        type: String,
        required: true
    },
})

const PC = Mongoose.model("newPC", PCSchema)
module.exports(PC)