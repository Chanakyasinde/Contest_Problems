function mainFunction(age ,gender){
     return checkMarriageEligibility(age,gender)
     .then((data)=>console.log(data))
    .catch((error)=>console.log(error))
}

function checkMarriageEligibility(age, gender) {
    return new Promise((resolve,reject)=>{
          if (age>=18 && gender=="female") {
               resolve("You are eligible for marriage in India.")
          } else if (age>=21 && gender=="male") {
               resolve("You are eligible for marriage in India.")
          } else {
               reject("You are not eligible for marriage in India.")
          }
     })
}
