function mainFunction(age){
   checkDrivingEligibility(age)
   .then((data) => console.log(data))
   .catch((error) => console.log(error))
}
function checkDrivingEligibility(age) {
   return new Promise((resolve,reject) => {
      if (age>=18) {
         resolve("You are eligible to drive in India.")
      } else {
         reject("You are not eligible to drive in India.")
      }
   })
}
