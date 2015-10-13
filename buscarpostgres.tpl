<!DOCTYPE html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta charset="utf-8">
		<title>Consulta PostgreSQL</title>
		<link rel="stylesheet" type="text/css" href="/static/hojaestilo.css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Indie+Flower' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<div id="encabezado">
			<a href="/"><h1>postgres</h1></a>
			<h2>Resultado de consulta:</h2>
		</div>
		<br>	
		<br>
		<br>
			
			%	for c1 in resultado1:
			% 	c1=str(c1)
				<li> {{c1}} </li>
				
			% end
			
		</div>
			
	</body>
</html>
