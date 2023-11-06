const input = require('sync-input');


function solution() {
    let name = input("Enter your name: ");
    let surname = input("Enter your surname: ");
    let message = input("Enter your message: ");
    let repeats = input("Enter number of repeats: ");

    for (let i = 0; i < repeats; i++) {
        console.log(`This is ${name} ${surname} and ${message}`);
    }

}

solution();