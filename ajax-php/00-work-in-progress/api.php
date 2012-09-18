<?php

$con = mysql_connect("127.0.0.1", "root", "root");
if (!$con) {
	die('Could not connect: ' . mysql_error());
}
mysql_select_db("wdd_db1", $con);

if ($_POST) {
	// update

	$status = array(
		'success' => false,
		'message' => '',
	);
	
	//print_r($_POST);
	$name = $_POST['name'];
	$email = $_POST['email'];
	$id = $_POST['id'];
	
	$query = "UPDATE `contacts` SET `name` = '$name', `email` = '$email' WHERE `id` = '$id';";
	
	$result = mysql_query($query);
	
	if($result) {
		$status['success'] = true;
		$status['message'] = 'Sucessfully updated contact.';
	} else {
		$status['message'] = 'Something went wrong.';
	}
	
	print json_encode($status);
	
} else {

	// Get
	if (isset($_GET['q'])) {
		$q = mysql_real_escape_string($_GET['q']);
	} else {
		$q = '';
	}

	$result = mysql_query("SELECT * FROM `contacts` WHERE `name` LIKE '%$q%'  LIMIT 0,100");

	$data = array();

	if ($result) {
		while ($row = mysql_fetch_array($result)) {

			$tem = array('id' => $row['id'], 'name' => $row['name'], 'email' => $row['email'], );

			array_push($data, $tem);
		}
	}

	print json_encode($data);

}

// close connection
mysql_close($con);
?>