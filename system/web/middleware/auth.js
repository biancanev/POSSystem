const jwt = require('jsonwebtoken')
const jwt_secret = process.env.JWT_SECRET

//Admin Auth Route
exports.adminAuth = (req, res, next) => {
    const token = req.cookies.jwt
    if (token) {
      jwt.verify(token, jwt_secret, (err, decodedToken) => {
        if (err) {
          return res.status(401).json({ message: "Not authorized" })
        } else {
          if (decodedToken.role !== "admin") {
            return res.status(401).json({ message: "Not authorized" })
          } else {
            next()
          }
        }
      })
    } else {
      return res
        .status(401)
        .json({ message: "Not authorized, token not available" })
    }
  }
  
  //User Auth Route(for basic page auth)
  exports.userAuth = (req, res, next) => {
    const token = req.cookies.jwt
    if (token) {
      jwt.verify(token, jwt_secret, (err, decodedToken) => {
        if (err) {
          return res.status(401).json({ message: "Not authorized" })
        } else {
          if (decodedToken.role !== "Basic") {
            return res.status(401).json({ message: "Not authorized" })
          } else {
            next()
          }
        }
      })
    } else {
      return res
        .status(401)
        .json({ message: "Not authorized, token not available" })
    }
  }


  