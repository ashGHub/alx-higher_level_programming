#!/usr/bin/node

if (process.argv.length == 2)
{
	console.log("Missing number of occurrences");
	return;
}

const rang = parseInt(process.argv[2]);

if (rang)
{

	for (let i = 0; i < rang; i++)
	{
		console.log("C is fun");
	}
}
