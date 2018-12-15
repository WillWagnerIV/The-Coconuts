<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Untitled Document</title>
</head>

<body><?php
function create_slug($string, $charset = 'utf-8'){
	$string = htmlentities($string, ENT_NOQUOTES, $charset, false); // convert accented characters to entities
	// strip unwanted parts of entities to leave unaccented character
    $string = preg_replace('~&([A-za-z])(?:acute|cedil|caron|circ|grave|orn|ring|slash|th|tilde|uml);~', '\1', $string);
    $string = preg_replace('~&([A-za-z]{2})(?:lig);~', '\1', $string);
    $string = preg_replace('~&[^;]+;~', '', $string); // remove other entities
    return preg_replace('~[\s!*\'();:@&=+$,/?%#[\]]+~', '-', $string); // replace spaces and illegal characters with hyphens
}
echo create_slug("This is a sample test")."<br>"; //returns 'This-is-a-sample-test'
echo create_slug("L'été? est là &amp; &eacute;");// returns 'L-ete-est-la-e'
?>
</body>
</html>