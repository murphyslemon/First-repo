'use strict';
let totalCandidates = +prompt("How many candidates are there?");
let listOfCandidates = []
let totalVoters = +prompt("How many voters are there?");

for (let i = 0; i < totalCandidates; i++) {
    listOfCandidates.push({
        name: prompt(`What is candidate ${i+1}'s name:`),
        votes: 0
    })
}

for (let i = 0; i < totalVoters; i++) {
    let vote = prompt("Enter your vote (one candidate's name):")
    if (vote in listOfCandidates) {
        name.votes += 1; //needs work
    }
}

listOfCandidates.forEach((candidate, index) => {
    console.log(`${candidate.name}, ${candidate.votes}`)
})
