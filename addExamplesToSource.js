//Require
var hanzi = require("hanzi");
const fs = require('fs');
const csv = require('@fast-csv/parse');

//Initiate
hanzi.start();
// var decomposition = hanzi.decompose('爱');
// console.log(decomposition);

// read a list of Radicals from a csv

const arr = Array(0);
const arr_char = Array(0);
// console.log(arr)


const data = fs.readFileSync('./data/source.csv', 'UTF-8');

const lines = data.split(/\r?\n/);
lines.forEach((line) => {
    arr.push(line.split("\t"));
});

for(let line of arr){
    if (hanzi.ifComponentExists(line[0])){
        var tmp = hanzi.getCharactersWithComponent(line[0]);
        if (typeof tmp == "object"){
            var tmp2 = tmp.slice(0,5);
            var tmp3 = tmp2.join(", ");
            arr_char.push(tmp3);
        }
        else {
            arr_char.push("");
        }
    }
    else{
        arr_char.push("");
    }
}

console.log(lines.length)
console.log(arr_char.length)
var text = "" 
for (i = 0, len = lines.length; i < len; i++) {
    if (lines[i]) {
        text += lines[i] + "\t" + arr_char[i] + "\n";
      }
  } 

fs.writeFile("./data/source_examples.csv", text, function (err) {
    if (err) return console.log(err);
    console.log('Finished!');
  });
// for loop with 
// hanzi.ifComponentExists(character/component);
//hanzi.getCharactersWithComponent( element ));
//make list to an string
//BONUS make a ruby with translation

//append to csv
