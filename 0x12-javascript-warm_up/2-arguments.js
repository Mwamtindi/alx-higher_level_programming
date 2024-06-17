#!/usr/bin/node
function printsMessage () {
  const argCount = arguments.length;

  if (argCount === 0) {
    console.log('No argument');
  } else if (argCount === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

printsMessage();
printsMessage(1);
printsMessage(1, 2, 3);
