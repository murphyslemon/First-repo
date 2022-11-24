'use strict';
let totalCandidates = +prompt("How many candidates are there?");
let listOfCandidates = []
let totalVoters = +prompt("How many voters are there?");

class Candidate {
    constructor(votes = 0) {
        this.name = prompt("Enter a candidate's name:");
        this.votes = votes;
    }
}

let candidate = []
for (let i = 0; i < totalCandidates; i++) {
    candidate[i] = new Candidate();
    listOfCandidates.push(candidate)
    console.log(candidate)
}

for (let i = 0; i < listOfCandidates.length; i++) {
    console.log((i+1) + ": " + listOfCandidates[i]);
}

for (let i = 0; i < totalVoters; i++) {
    this.name = prompt("Enter a candidate's name(your vote):")
}
//unfinished