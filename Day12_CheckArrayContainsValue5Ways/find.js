// find() -- returns value of
// first element that matches the condition

const languages = ['python', 'java', 'c#', 'js' , 'c++','python']
const value = languages.find(lang => lang == 'java')
console.log(value) // java

const value = languages.find(lang => lang == 'c')
console.log(value) // undefined

