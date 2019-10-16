var exp=require("express")
var obj=exp();
var axios=require("axios")
obj.get("/home",(req,res)=>{
    res.send("hello");
})
obj.listen(3000,()=>{console.log("built")})