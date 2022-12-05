let new_str;
const question = document.getElementById("calculation").value;;
const p = document.querySelector('#result');
const button = document.querySelector('button');

button.addEventListener('click', function(evt) {
    if (question.includes("+")) {
        new_str = question.split("+");
        let x = +(new_str[0]);
        let y = +(new_str[1]);
        let z = x + y;
        console.log(z);
        console.log(x);
        console.log(y);
    } else if (question.includes("-")) {
        new_str = question.split("-");
        let x = +(new_str[0]);
        let y = +(new_str[1]);
        p.innerHTML = `Answer: ${x - y}`
    } else if (question.includes("*")) {
        new_str = question.split("*");
        let x = +(new_str[0]);
        let y = +(new_str[1]);
        p.innerHTML = `Answer: ${x * y}`
    } else if (question.includes("/")) {
        new_str = question.split("/");
        let x = +(new_str[0]);
        let y = +(new_str[1]);
        p.innerHTML = `Answer: ${x / y}`
    }
})

console.log(question)
//doesnt work
