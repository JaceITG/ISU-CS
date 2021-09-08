let data = [
    "Jace",
    "Williams",
    "jwilliams287@sycamores.indstate.edu",
    "cs17028",
    8,
    24,
];

console.log(`My name is ${data[0]} ${data[1]}, my email address is ${data[2]}, my CS Server account is ${data[3]}, and my birthday is ${data[4].toString().padStart(2, '0')}-${data[5].toString().padStart(2, '0')}.`);
