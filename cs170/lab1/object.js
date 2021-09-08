let data = {
    fName: "Jace",
    lName: "Williams",
    email: "jwilliams287@sycamores.indstate.edu",
    uname: "cs17028",
    bMonth: 8,
    bDay: 24,
};

console.log(`My name is ${data.fName} ${data.lName}, my email address is ${data.email}, my CS Server account is ${data.uname}, and my birthday is ${data.bMonth.toString().padStart(2, '0')}-${data.bDay.toString().padStart(2, '0')}.`);
