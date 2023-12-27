const newPC = require('../models/newPC')

function calculate(price, perf1, perf2){
    /** 
     * CPU: 20-25
     * GPU: 20-25
     * RAM: 10
     * MOBO: 15-20
     * CASE: 10
     * STORAGE: 5
     * PSU: 
     * OTHER: 5-10
     * **/
}

exports.newDesign = async (req, res, next) => {
    const {cpu, cooler, motherboard, ram, gpu, pccase, cooling, os, associatedID} = req.body
    try{
        await newPC.create({
            cpu, cooler, motherboard, ram, gpu, pccase, cooling, os, associatedID
        }).then((pc) => {
            res.status(200).json({
                message: "Design successfully created",
                pc
            })
        })
    }catch(err){
        return res.status(500).json({message: "The server encountered an error"})
    }
}

exports.getDesign = async (req, res, next) => {
    const {id} = req.body
    try{
        const pc = await newPC.findById(id)
        
    }catch(err){
        return res.status(500).json({message: "The server encountered an error"})
    }
}