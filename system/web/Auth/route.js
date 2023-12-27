const express = require("express")
const router = express.Router()
const { register, login, update, deleteUser } = require("./Auth")
const { adminAuth } = require("../middleware/auth")

// Routes
router.route("/register").post(register)
router.route("/login").post(login)
router.route("/update").put(update)
router.route("/deleteUser").delete(deleteUser)
router.route("/update").put(adminAuth, update)
router.route("/deleteUser").delete(adminAuth, deleteUser)

//Export
module.exports = router