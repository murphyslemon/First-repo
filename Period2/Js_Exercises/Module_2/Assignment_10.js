'use strict';
let totalCandidates = +prompt("How many candidates are there?");
let listOfCandidates = [];
let totalVoters = +prompt("How many voters are there?");

for (let i = 0; i < totalCandidates; i++) {
    listOfCandidates.push({
        name: prompt(`What is candidate ${i+1}'s name:`),
        votes: 0
    })
}

for (let i = 0; i < totalVoters; i++) {
    let vote = prompt(`Enter voter ${i+1}'s vote (one candidate's name):`);
    for (let i = 0; i < listOfCandidates.length; i++) {
        if (vote === listOfCandidates[i]["name"]) {
            listOfCandidates[i]["votes"]++;
        }
    }
}

let winningVotes = 0
let winner = ''
for (let i = 0; i < listOfCandidates.length; i++) {
    if (listOfCandidates[i]["votes"] >= winningVotes) {
        winningVotes = listOfCandidates[i]["votes"]
        winner = listOfCandidates[i]["name"]
    }
}

console.log(`The winner is ${winner} with ${winningVotes} votes.`)
console.log('Results:')
listOfCandidates.forEach((candidate, index) => {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
})


