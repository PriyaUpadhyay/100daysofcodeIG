// every() --  return true if all elements pass a condition
const magicNos = [2, 10, 18, 36, 54, 86]

const result =  magicNos.every(num => num %2 == 0)
console.log(result) //true

const result =  magicNos.every(num => num > 3)
console.log(result) // false
