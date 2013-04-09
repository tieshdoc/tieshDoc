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
                    <input type="text" placeholder="name" name="postername">
                </div>
                <div class="control-group">
                    <textarea rows="3" name="talkcontent"></textarea>
                </div>
                <div class="control-group">
                    <button type="submit" class="btn">submit</button>
                </div>
            </form>
        </div>

    </div>
</body>
</html>
