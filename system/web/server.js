/** *
 * Basic HTTP server setup. Currently using NodeJS backend and EJS rendering for frontend.
 * Potentially switch to ReactJS for frontend later.
*/

//import dotenv to read environment variables
require("dotenv").config()
//import ExpressJS
const express = require("express")
//import session manager
const sessions = require("express-session")

const app = express()

const sessionSecret = process.env.SESSION_SECRET
const oneDay = 1000 * 60 * 60 * 24

app.use(express.json())
app.use("/api/auth", require("./Auth/route"))
app.use(sessions({
    secret: sessionSecret,
    saveUninitialized: false,
    cookie: {maxAge: oneDay},
    resave: false
}))

var session;

const PORT = 5000
const connectDB = require("./db")
const { adminAuth, userAuth } = require("./middleware/auth.js");
app.set("view engine", "ejs")

const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/admin", adminAuth, (req, res) => res.send("Admin Route"));
app.get("/basic", userAuth, (req, res) => res.send("User Route"));

app.get("/", (req, res) => res.render("home"))
app.get("/register", (req, res) => res.render("register"))
app.get("/login", (req, res) => res.render("login"))
app.get("/admin", adminAuth, (req, res) => res.render("admin"))
app.get("/basic", userAuth, (req, res) => {
    req.session.userid = req.cookies.jwt
    console.log(req.session.userid)
    res.render("user")

})
app.get("/build", userAuth, (req, res) => res.render(""))

app.get("/logout", (req, res) => {
    res.cookie("jwt", "", { maxAge: "1" })
    req.session.destroy()
    res.redirect("/")
  })

connectDB();

const server = app.listen(PORT, () =>
    console.log(`Server Connected to port ${PORT}`)
)

process.on("unhandledRejection", err => {
    console.log(`An error occurred: ${err.message}`)
    server.close(() => process.exit(1))
})
