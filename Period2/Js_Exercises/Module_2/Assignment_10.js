'use strict';
let totalCandidates = +prompt("How many candidates are there?");
let listOfCandidates = []

class Candidate {
    constructor(votes = 0) {
        this.name = prompt("Enter a candidate's name:");
        this.votes = votes;
    }
}

let candidate = []
for (let i = 0; i < totalCandidates; i++) {
    candidate = new Candidate();
    listOfCandidates.push(candidate)
    console.log(candidate)
}

for (let i = 0; i < listOfCandidates.length; i++) {
    console.log((i+1) + ": " + listOfCandidates[i]);
}
//unfinished