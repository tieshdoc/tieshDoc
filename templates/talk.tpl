$def with (tf)
<!DOCTYPE HTML>
<html>
    <title>TieshTalk</title>
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
<body>
    <div class="container">
        <div>
            <h1>Let"s talk here</h1>
            <p>This is designed to replace tucaoBook...</p>
        </div>
        <div>
            <form class="form-horizontal" action="/talk" method="post">
                <div class="control-group">
                    $:tf.postername.render()
                </div>
                <div class="control-group">
                    $:tf.talkdata.render()
                </div>
                <div class="control-group">
                    $:tf.submit.render()
                </div>
            </form>
        </div>

    </div>
</body>
</html>
