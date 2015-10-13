<!DOCTYPE html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta charset="UTF-8">
		<title>Consulta Oracle</title>
		<link rel="stylesheet" type="text/css" href="/static/hojaestilo.css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Indie+Flower' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<div id="encabezado">
			<a href="/"><h1>Mongo</h1></a>
			<h2>Resultado de consulta:</h2>
		</div>	
			%	for c1 in resultado3.find():
				<li> {{c1}} </li>
				
			% end
			
		</div>
			
	</body>
</html>


