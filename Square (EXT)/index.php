<?php
# Variable import

require('creds.php');


# Select an API and endpoint to get started.

use Square\SquareClient;

$config = [
    'accessToken' => $accessToken,
    'environment' => 'sandbox'
];
$client = new SquareClient($config);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba API Square</title>
</head>
<body>
    
</body>
</html>