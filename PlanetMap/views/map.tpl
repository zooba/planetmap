<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planet Map</title>
    <link rel="stylesheet" type="text/css" href="/static/site.css" />

    <style type="text/css">
        div.solar-system {
            background-color: black;
            width: 600px;
            height: 600px;
            float: left;
        }

        img#sun {
            position: absolute;
            left: 250px;
            top: 250px;
        }
        % for name, value in [('mercury', mercury), ('venus', venus), ('earth', earth), ('mars', mars), ('jupiter', jupiter), ('saturn', saturn), ('uranus', uranus), ('neptune', neptune)]:
        img#{{name}} { position: absolute; left: {{value[0] * 500}}px; top: {{value[1] * 500}}px; }
        % end

        div.controls {
            float: left;
            width: 150px;
            margin: 15px;
        }

        form {
            width: 100%;
            margin-top: 2em;
            padding: 4%;
            border: black 1px solid;
        }

        form p {
            margin: 0;
        }
    </style>
</head>

<body>
    <div class="solar-system">
        % for name in ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']:
        <img src="/static/{{name}}.png" id="{{name}}" alt="{{name.title()}}"/>
        % end
    </div>

    <div class="controls">
        % for k, d in [('Tomorrow', tomorrow), ('Next week', nextweek), ('Next month', nextmonth), ('Next year', nextyear)]:
        % if d:
        <p>
            <a href="/map?source={{source}}&apikey={{apikey}}&{{format(d, 'year=%Y&month=%m&day=%d')}}">
                {{k}}<br />({{format(d, '%Y-%b-%d')}})
            </a>
        </p>
        % end
        % end

        <form method="get" action="/map">
            <input type="hidden" name="source" value="{{source}}" />
            <input type="hidden" name="apikey" value="{{apikey}}" />
            <p><label>Year: <input name="year" value="{{year}}" type="number" /></label></p>
            <p><label>Month: <input name="month" value="{{month}}" type="number" /></label></p>
            <p><label>Day: <input name="day" value="{{day}}" type="number" /></label></p>
            <p><input type="submit" value="Update" /></p>
        </form>
    </div>

	<p class="small">
    Images based on works by
    <a href="http://www.astro.cornell.edu/~randerson/Inreach%20Web%20Page/inreach/uranus.html">Calvin J. Hamilton</a>
    and <a href="http://www.nasa.gov/mission_pages/sunearth/news/News111312-m6flare.html">NASA</a>.
    </p>
</body>
</html>
