<?php       

$a = 1145;
do{
    $b = rand(10000, 99999999);    
}
while ($b%$a>0);

echo "Random value is " . $b;
