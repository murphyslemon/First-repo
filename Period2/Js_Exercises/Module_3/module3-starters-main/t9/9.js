// this works too
// const button = document.getElementById('start');
// const answer = document.querySelector('#result');

// button.addEventListener('click', function () {
//     let x = document.getElementById('calculation').value;
//     let result = Function('return ' + x)();
//     answer.innerHTML = result;
// })

document.querySelector('button').addEventListener('click', calculate);

function calculate() {
    const userInput = document.getElementById('calculation').value;
    let sortedInput;
    let result;

    if (userInput.includes("+")) {
        sortedInput = userInput.split("+");
        result = +(sortedInput[0]) + +(sortedInput[1]);
    }
    else if (userInput.includes("-")) {
        sortedInput = userInput.split("-");
        result = +(sortedInput[0]) - +(sortedInput[1]);
    }
    else if (userInput.includes("*")) {
        sortedInput = userInput.split("*");
        result = +(sortedInput[0]) * +(sortedInput[1]);
    }
    else if (userInput.includes("/")) {
        sortedInput = userInput.split("/");
        result = +(sortedInput[0]) / +(sortedInput[1]);
    }
    document.getElementById('result').innerHTML = result;
}
