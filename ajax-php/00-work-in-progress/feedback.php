<?php

if($_POST) {
	
	$validation = array(
		'email' => array(
			'status' => false,
			'error' => false, 
		),
		'name' => array(
			'status' => false,
			'error' => false, 
		),
		'comment' => array(
			'status' => false,
			'error' => false, 
		),
	);
	
	$name = $_POST['name'];
	$email = $_POST['email'];
	$comment = $_POST['comment'];
	
	$validation['name'] = validate_name($name);
	$validation['email'] = validate_email($email);
	
	print json_encode(array(
		'validation' => $validation,
	));
	
}

function validate_name($name) {
	
	$error = false;
	
	if(strlen($name) < 2) {
		$error = 'Name too short.';
	};
	if(strlen($name) > 20) {
		$error = 'Name too long.';
	};
	if(strlen($name) == 0) {
		$error = 'Name must not be empty.';
	};
	
	if ($error) {
		return array(
			'status' => false,
			'error' => $error,
		);
	} else {
		return array(
			'status' => true,
			'error' => false,
		);
	};
	
}

function validate_email($email) {
	
	$error = false;

	if(strlen($email) == 0) {
		$error = 'Email must not be empty.';
	};

	if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
	    $error = "Email seems to be invalid";
	}

	if ($error) {
		return array(
			'status' => false,
			'error' => $error,
		);
	} else {
		return array(
			'status' => true,
			'error' => false,
		);
	};
	
}
function validate_comment($comment) {
	
	$error = false;
	
	if(strlen($comment) < 2) {
		$error = 'Comment too short. Min 2 chars';
	};
	if(strlen($name) > 2000) {
		$error = 'Comment too long. 2000 chars max.';
	};
	if(strlen($comment) == 0) {
		$error = 'Comment must not be empty.';
	};
	
	if ($error) {
		return array(
			'status' => false,
			'error' => $error,
		);
	} else {
		return array(
			'status' => true,
			'error' => false,
		);
	};
	
}



?>
