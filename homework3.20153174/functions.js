console.log("hello homework3");

function stringToInt(input)
{
	return parseInt(input);
}

function maskNumber(input) 
{
	mask_number="";
	for(var i=0;i<7;i++)
		mask_number+=input[i];
	for(var j=7;j<11;j++)
		mask_number+="*";		
	return mask_number;
}

function getAverage(input_array) 
{
	var sum=0;

	for(var i=0;i<input_array.length;i++)
		sum+=input_array[i];
        var avg=sum/input_array.length;	
	return avg;
}

function isMultipleSeven(input) 
{
	if(input%7==0)
		return true;
	else
		return false;
}

function operation(operator, data1, data2)
{
	if(operator=="add")
		return data1+data2;
	else if(operator=="substract")
		return data1-data2;
	else if(operator=="divide")
		return data1/data2;
	else if(operator=="multiply")
		return data1*data2;
	else
		console.log("Not Supported");
}

function triangleMtn(input)
{
	num="";
	for(var i=0;i<input;i++)
		{
			num+="*";
			console.log(num);
		}
}