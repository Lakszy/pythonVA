// how to reverse a string 
var str="Lakshay Is A Bad Boy"
var stry=""
str.split(" ")
.forEach(function(word){
    var sting=word.split("").reverse().join("")
    stry+=sting
    stry+=" "
})
console.log(stry)

// How to empty an array without looping through it using pop
var arr=[1,2,3,4,5,6,7,8,9]
arr.length=0;
console.log(arr)

// check number is integer or not
var number = 12.2
console.log(number%1 === 0 ?"Is integer":"is not")


// dupcate an array
var arr=[1,2,3,4,5,6,7,8,9]
console.log(arr.concat(arr))


// reverse a function
function reversekaro(num){
   return Number(num.toString().split("").reverse().join(""))
}

console.log(reversekaro(321))

// return in ahabeticaL order
var String ="lakshay"
console.log(String.split("").sort())
