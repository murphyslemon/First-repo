'use strict';
let totalCandidates = +prompt("How many candidates are there?");
let listOfCandidates = []

class Candidate {
    constructor(votes = 0) {
        this.name = prompt("Enter a candidate's name:");
        this.votes = votes;
    }
}

var candidate = []
for (let i = 0; i < totalCandidates; i++) {
    candidate[i+1] = new Candidate();
    listOfCandidates.push(candidate[i+1])
    console.log(candidate[i+1])
}
//unfinished