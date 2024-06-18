#!/usr/bin/node
const fileSystem = require('fs');
const firstFile = fileSystem.readFileSync(process.argv[2], 'utf8');
const secondFile = fileSystem.readFileSync(process.argv[3], 'utf8');

fileSystem.writeFileSync(process.argv[4], firstFile + secondFile);
