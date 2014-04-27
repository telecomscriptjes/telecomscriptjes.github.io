var header = 'The script is now being loaded...\n';
window.jqconsole = $('#console').jqconsole(header, '');


inputCallback = function(handler){
	jqconsole.Prompt(true, function(input) { 
		console.log(input)
		handler(input)
	});
}

outputCallback = function(data){
	jqconsole.Write(data);
}

var jsrepl = new JSREPL({  
	input: inputCallback,  
	output: outputCallback,
	error: outputCallback, 
});

jsrepl.loadLanguage('python', function () {  
	jqconsole.Write("Python Loaded\n\n")
	jsrepl.eval('import math')
	jsrepl.eval('def log10(value):\n' +
				'    return math.log(value)/math.log(10)\n'+
				'math.log10 = log10')

	script = $('#python-script').text()
	jsrepl.eval(script)
});