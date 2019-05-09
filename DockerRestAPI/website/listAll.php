<html>
    <head>
        <title>Open and Close Times</title>
    <body>
        <h1>Open and Close Times</h1>
        <ul>
            <?php
            $json = file_get_contents('./ListAll');
            $obj = json_decode($json);
	          $open_times = $obj->open_time
            foreach ($open_times as $o) {
                echo "<li>$o</li>";
            }
            ?>
        </ul>
    </body>
</html>
