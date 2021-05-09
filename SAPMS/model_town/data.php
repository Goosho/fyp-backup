<?php
$data_reading = "Date,Temperature,Humidity,PM1,PM2.5,PM10,Location";
$read_date = date("Y-m-d") ;
$read_time = date("h:i:sa");


if($_GET['temp'] != '' and  $_GET['humi'] != ''and  $_GET['pm1'] != ''and  $_GET['pm25'] != ''and  $_GET['pm10'] != ''and  $_GET['co'] != '' and  $_GET['NOx'] != ''  and  $_GET['Location'] != ''  ){

	$temp = $_GET['temp'];
	$humi = $_GET['humi'];
	$pm1 =  $_GET['pm1'] ;
	$pm25 =  $_GET['pm25'];
	$pm10 =   $_GET['pm10'];
	$co = $_GET['co'] ;
	$NOx = $_GET['NOx'];
	$Location = $_GET['Location'];
	$data_reading = "$read_date,$read_time,$temp,$humi,$pm1,$pm25,$pm10,$co,$NOx,$Location\n";
}

$file = fopen("model_town.csv","a");

fwrite($file,$data_reading);

fclose($file);

$command = escapeshellcmd('python script.py');
    $output = shell_exec($command);
$command = escapeshellcmd('python script2.py');
    $output = shell_exec($command);
$command = escapeshellcmd('python script3.py');
    $output = shell_exec($command);

?>
