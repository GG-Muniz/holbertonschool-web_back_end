export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }

  export function getLast() {
    return ' is okay';
  }

  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();

    return combination;
  }
    export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();

    return combination;
  }

// Call the functions and print the output
console.log(taskFirst() + ' ' + taskNext());
