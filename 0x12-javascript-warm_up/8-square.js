#!/usr/bin/node

const sz = parseInt(process.argv[2]);

if (sz)
{

	for (let i = 0; i < sz; i++)
	{
		let s = "";
		for (let j = 0;  j < sz; j++)
		{
			s = s + "X";
		}
		console.log(s);
	}
}
else
{
	console.log("Missing size");
}
