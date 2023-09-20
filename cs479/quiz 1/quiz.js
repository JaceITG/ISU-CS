

function findFirstEven(li) {

    li.forEach(x => {
        if (x % 2 == 0) {
            return x;
        }
    });
}
let li = [1, 2, 3, 4, 5];
console.log(findFirstEven(li));
