/** *
 * Basic HTTP server setup. Currently using NodeJS backend and EJS rendering for frontend.
 * Potentially switch to ReactJS for frontend later.
*/

//import dotenv to read environment variables
require("dotenv").config();
//import ExpressJS
const express = require("express");
//import session manager
const session = require("express-session");

const app = express();

const sessionSecret = process.env.SESSION_SECRET;
const oneDay = 1000 * 60 * 60 * 24;

app.use(express.json());

app.use(session({
    secret: sessionSecret,
    saveUninitialized: false,
    cookie: {maxAge: oneDay},
    resave: false
}));

app.use("/api/auth", require("./Auth/route"));



const PORT = 5000;
const connectDB = require("./db");
const { adminAuth, userAuth } = require("./middleware/auth.js");
app.set("view engine", "ejs");

const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/", (req, res) => res.render("home"));
app.get("/register", (req, res) => res.render("register"));
app.get("/login", (req, res) => res.render("login"));
app.get("/admin", adminAuth, (req, res) => res.render("admin"));
app.get("/user", userAuth, (req, res) => {
    res.render("user")

});
app.get("/logout", (req, res) => {
    res.cookie("jwt", "", { maxAge: "1" })
    req.session.destroy()
    res.render("logout")
  });

connectDB();

const server = app.listen(PORT, () =>
    console.log(`Server Connected to port ${PORT}`)
);

process.on("unhandledRejection", err => {
    console.log(`An error occurred: ${err.message}`)
    server.close(() => process.exit(1))
});

