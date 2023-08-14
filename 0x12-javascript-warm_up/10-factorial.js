#!/usr/bin/node


const a = parseInt(process.argv[2]);
console.log(fact(a));

function fact(num)
{
	if (num == 0 || num == 1 || !num)
	{
		return 1;
	}
	return num * fact(num - 1);
}
