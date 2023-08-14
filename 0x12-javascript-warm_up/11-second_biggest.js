#!/usr/bin/node


if (process.argv.length <= 3)
{
	console.log(0);
	return;
}

let max = parseInt(process.argv[2]);
let secMax = max;
for (let i = 1; i < process.argv.length; i++)
{
	let n = parseInt(process.argv[i]);
	if (n > max)
	{
		secMax = max;
		max = n;
	}
}
console.log(secMax);
