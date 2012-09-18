<?php

// db settings
$db_host = '127.0.0.1';
$db_user = 'root';
$db_pass = 'root';
$db_database = 'wdd_db1';

// connect
$con = mysql_connect($db_host, $db_user, $db_pass);
if (!$con) {
	die('Could not connect: ' . mysql_error());
}
// and select the working db
mysql_select_db($db_database, $con);



if ($_POST) {
	// POST request, se we have an update (or insert)

	$status = array(
		'success' => false,
		'message' => '',
	);
	
	$name = $_POST['name'];
	$email = $_POST['email'];
	$id = (isset($_POST['id']) ? $_POST['id'] : false);
	
	if($id AND $name AND $email) {
		// We have an id - > update query
		$query = "UPDATE `contacts` SET `name` = '$name', `email` = '$email' WHERE `id` = '$id';";
	} else if($name AND $email){
		// No id provided, so we assume it's an insert
		$query = "INSERT INTO `contacts` (`id`, `name`, `email`) VALUES (NULL, '$name', '$email')";
	}
	
	if(!$query) {
		
		$status['message'] = 'Invalid input.';
		
	} else {
		
		$result = mysql_query($query);
		if($result) {
			$status['success'] = true;
			$status['message'] = 'Sucessfully ' . (($id) ? 'updated' : 'created') . ' contact.';
		} else {
			$status['message'] = 'Something went wrong.';
		}
	}
	
	
	// send back the result as json encoded data
	print json_encode($status);
	
} else {
	// GET request
	
	if (isset($_GET['q'])) {
		$q = mysql_real_escape_string($_GET['q']);
	} else {
		$q = false;
	}

	// provide an empty array to fill with db results
	$data = array();
	
	// only do the query if there is $q
	if($q) {
		$result = mysql_query("SELECT * FROM `contacts` WHERE `name` LIKE '%$q%'  LIMIT 0,100");
		if ($result) {
			while ($row = mysql_fetch_array($result)) {
	
				$tem = array('id' => $row['id'], 'name' => $row['name'], 'email' => $row['email'], );
	
				array_push($data, $tem);
			}
		}
	}
	
	// send back the result as json encoded data
	print json_encode($data);

}

// close connection
mysql_close($con);
?>