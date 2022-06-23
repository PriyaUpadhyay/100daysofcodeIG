// Array.indexOf() 
// returns index if found, else -1

const languages = ['python', 'java', 'c#', 'js' , 'c++']
languages.indexOf('c#') // 2
languages.indexOf('python') // 0
languages.indexOf('c') // -1

// search from the desired location
languages.indexOf('c#',1) // 2
languages.indexOf('c#',2) // 2
languages.indexOf('c#',3) //-1
