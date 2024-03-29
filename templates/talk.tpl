$def with (tform, talklist)
<!DOCTYPE HTML>
<html>
<head>
    <title>TieshTalk</title>
    <meta charset="utf-8" />
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
</head>
<body onload="setName()">
    <div class="container">
        <div>
            <h1>Let's talk here</h1>
            <p>This is designed to replace tucaoBook...</p>
        </div>
        <div>
            <form class="form-horizontal" action="/talk" method="post" onsubmit="return checkInput()">
                <div class="control-group">
                    $:tform.postername.render()
					<span id="checkName" style="color:red"></span>
                </div>
                <div class="control-group">
                    $:tform.talkdata.render()
					<span id="checkData" style="color:red"></span>
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
	
	<script>
		function checkInput() {
			var flag = false;
			if (document.getElementById("postername").value=="") {
				document.getElementById("checkName").innerHTML="please input your name here!";
				flag = true;
			}
			else {
				document.getElementById("checkName").innerHTML="";
			}
			if (document.getElementById("talkdata").value=="") {
				document.getElementById("checkData").innerHTML="please input your comments here!"
				flag = true;
			}
			else {
				document.getElementById("checkData").innerHTML="";
			}
			if (flag)
				return false;
			if (typeof(Storage)!=="undefined")
				localStorage.name = document.getElementById("postername").value;
		}
		
		function setName() {
			if (typeof(Storage)!=="undefined")
				if (localStorage.name)
					document.getElementById("postername").value=localStorage.name;
		}
	</script>
</body>
</html>
