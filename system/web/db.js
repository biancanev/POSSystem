const Mongoose = require("mongoose")
const localDB = 'mongodb://127.0.0.1:27017/role_auth'
const connectDB = async () => {
    try{
        await Mongoose.connect(localDB, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        console.log("DB Connected")
    } catch (err){
        console.log(err)
    }
}
module.exports = connectDB