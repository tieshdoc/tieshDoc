$def with (tform, talklist)
<!DOCTYPE HTML>
<html>
    <title>TieshTalk</title>
    <meta charset="utf-8" />
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
<body>
    <div class="container">
        <div>
            <h1>Let's talk here</h1>
            <p>This is designed to replace tucaoBook...</p>
        </div>
        <div>
            <form class="form-horizontal" action="/talk" method="post">
                <div class="control-group">
                    $:tform.postername.render()
                </div>
                <div class="control-group">
                    $:tform.talkdata.render()
                </div>
                <div class="control-group">
                    <button class="btn" type="submit">Submit</button>
                </div>
            </form>
        </div>
        <div>
        $for onetalk in talklist:
            <div class="well">
            $for k, v in onetalk.iteritems():
                <p><strong>$(k):</strong> $(v)</p>
            </div>
        </div>

    </div>
</body>
</html>
