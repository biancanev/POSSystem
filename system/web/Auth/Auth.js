/*
Basic CRUD operations for user authenication
*/

const User = require("../models/user")
const bcrypt = require("bcryptjs")
const jwt = require('jsonwebtoken')
const jwt_secret = process.env.JWT_SECRET


//Register function
exports.register = async (req, res, next) => {
    const { username, password, email } = req.body
    if (password.length < 6) {
      return res.status(400).json({ message: "Password less than 6 characters" })
    }
    try {
      bcrypt.hash(password, 10).then(async (hash) => {
        await User.create({
          username,
          password: hash,
          email,
        }).then((user) => {
            const maxAge = 3 * 60 * 60
            const token = jwt.sign({id: user._id, username, role: user.role}, jwt_secret, {expiresIn: maxAge})
            res.cookie("jwt", token, {httpOnly: true, maxAge: maxAge * 1000})
            res.status(200).json({
            message: "User successfully created",
            user,
            })
        })
      })
    }catch (err) {
      res.status(401).json({
        message: "User not successfully created: " + err.message,
        error: err.mesage,
      })
    }
  }

//Login function
exports.login = async (req, res, next) => {
  const {username, password} = req.body
  if(!username || !password){
    return res.status(400).json({
      message: "Username or Password is not entered"
    })
  }
  try{
    const user = await User.findOne({username})
    if(!user){
      res.status(401).json({
        message: "Login unsuccessful",
        error: "User not found"
      })
    }else{
      bcrypt.compare(password, user.password).then(function (result){
        if(result){
          const maxAge = 3 * 60 * 60
          const token = jwt.sign({id: user._id, username, role: user.role}, jwt_secret, {expiresIn: maxAge})
          res.cookie("jwt", token, {httpOnly: true, maxAge: maxAge * 1000})
          req.session.regenerate(function (err) {
            if(err) next(err)
            req.session.user = username;
            req.session.save(function (err) {
              if(err) return next(err)
            });
          });
          res.status(201).json({
            message: "Login successful",
            user
          })
        }else{
            res.status(401).json({
            message: "Login not successful"
          })
        }
        })
      }
    }catch(err){
    res.status(400).json({
      message: "An error occurred",
      error: err.message
    })
  }
}

//Update function
exports.update = async (req, res, next) => {
  const { role, id } = req.body;
  // First - Verifying if role and id is presnt
  if (role && id) {
    // Second - Verifying if the value of role is admin
    if (role === "admin") {
      // Finds the user with the id
      await User.findById(id).then((user) => {
          // Third - Verifies the user is not an admin
          if (user.role !== "admin") {
            user.role = role;
            user.save((err) => {
              //Monogodb error checker
              if (err) {
                res.status(400).json({ 
                  message: "An error occurred", 
                  error: err.message 
                });
                process.exit(1)
              }
              res.status(201).json({ message: "Update successful", user })
            })
          }else {
            res.status(400).json({ message: "User is already an Admin" })
          }
        }).catch((error) => {
          res.status(400).json({ 
            message: "An error occurred", 
            error: error.message })
        })
      }
    }
  }

//Delete function
exports.deleteUser = async (req, res, next) => {
  const {id} = req.body
  try{
    await User.findById(id).then(user => user.deleteOne()).then(user => res.status(201).json({
      message: "User successfully deleted", user
    }))
  }catch(err){
    res.status(401).json({
      message: "An error occurred",
      error: err.message
    })
  }
}

//GET function for web
exports.getUsers = async (req, res, next) => {
  await User.find({})
    .then(users => {
      const userFunction = users.map(user => {
        const container = {}
        container.username = user.username
        container.role = user.role
        return container
      })
      res.status(200).json({ user: userFunction })
    })
    .catch(err =>
      res.status(401).json({ message: "Not successful", error: err.message })
    )
}

exports.findUser = async (req, res, next) => {
  const username = req.body
  await User.findOne(username).then(foundUser => {
      res.status(200).json({user: foundUser})
    }
  ).catch(err => {
    res.status(401).json({message: "Not found", error: err.message})
  })
}