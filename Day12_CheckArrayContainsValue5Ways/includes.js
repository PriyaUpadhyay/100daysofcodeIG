// includes() -- returns true if present, else false
const languages = ['python', 'java', 'c#', 'js' , 'c++','python']
languages.includes('c#') // true


// search from a desired index
languages.includes('java',3) // false


// includes() vs indexOf() with NaN
const arr = [NaN]
arr.includes(NaN) // true

arr.indexOf(NaN) // -1

