<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planet Map</title>
    <link rel="stylesheet" type="text/css" href="/static/site.css" />

    <style type="text/css">
        form {
            width: 80%;
        }
        form input {
            width: 100%;
        }

        form input[type=submit] {
            width: auto;
            align-self: center;
        }
    </style>
</head>

<body>
    <form method="get" action="/map">
        <p><label>Source: <input name="source" /></label></p>
        <p><label>API Key: <input name="apikey" /></label></p>
        <p><input type="submit" value="Submit" /></p>
    </form>
</body>
</html>
