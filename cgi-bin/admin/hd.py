#!/usr/bin/python
import commands
import cgi, os
import cgitb; cgitb.enable()
commands.getoutput("cd /root/Desktop/")
#to show total HD in GB----------------------------------------------------------------------------
totHD=commands.getoutput("df -H --total | grep total  | awk '{s+=$2} END {print s}'")
#to show used HD in GB
usedHD=commands.getoutput("df -H --total | grep total  | awk '{s+=$3} END {print s}'")
#to show free HD space in GB
freeHD=commands.getoutput("df -H --total | grep total  | awk '{s+=$4} END {print s}'")
#to show Available HD space in persantage(%)
persantageHD=commands.getoutput("df -H --total | grep total  | awk '{s+=$5} END {print s}'")

#To show total Ram in GB---------------------------------------------------------------------------
totRAM=commands.getoutput("free -m | grep Mem  | awk '{s+=$2} END {print s/1024}'")
#To show used RAM space in GB
usedRAM=commands.getoutput("free -m | grep Mem  | awk '{s+=$3} END {print s/1024}'")
#To show Free RAM space in GB
freeRAM=commands.getoutput("free -m | grep Mem  | awk '{s+=$4} END {print s/1024}'")  
persantageRAM1=(float(usedRAM)*100)/float(totRAM)
persantageRAM=int(round(persantageRAM1))
persantageRAM=str(persantageRAM)

print "Content-Type: text/html\n"
print ""
print """
<!DOCTYPE html>
<html>

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">


<script type="text/javascript">
function mov1() {
  var elem = document.getElementById("myBar1");   
  var width = 1;
  var id = setInterval(frame, 20);
  function frame() {
    if (width >= """+persantageHD+""") {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
      document.getElementById("demo1").innerHTML = width * 1  + '%';
    }
  }
}
function mov2() {
  var elem = document.getElementById("myBar2");   
  var width = 1;
  var id = setInterval(frame, 20);
  function frame() {
    if (width >= """+persantageRAM+""") {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
      document.getElementById("demo2").innerHTML = width * 1  + '%';
    }
  }
}
</script>
<body>
	<ul class="w3-navbar w3-blue">
		<h2>System information</h2>
	</ul>
	<br/>
	
	<div class="w3-container" onload="mov1();">
		<div class="w3-container w3-border">
  		<p><h4>Server Storage information</h4><p>
		<div class="progress w3-progress-container w3-smal">
			<div id="myBar1" class="progress-bar progress-bar-striped active" style='width:"""+persantageHD+"""%'>
     				<div id="demo1" class="w3-container w3-text-white">"""+persantageHD+"""%</div>					
			</div>
		</div>
		<h5 class="w3-border" >Total memory :"""+totHD+""" GB</h5>
		<h5 class="w3-border" >Total used :"""+usedHD+""" GB</h5>
		<h5 class="w3-border" >Total free :"""+freeHD+""" GB</h5>
		<button class="w3-btn w3-dark-grey w3-right " onclick="mov1()">Refresh</button> 
		</div>
	</div>

	<div class="w3-container">
		<div class="w3-container w3-border">
  		<p><h4>Server RAM information</h4><p>
		<div class="progress w3-progress-container w3-smal">
			<div id="myBar2" class="progress-bar progress-bar-striped active" style='width:"""+persantageRAM+"""%'>
     				<div id="demo2" class="w3-container w3-text-white">"""+persantageRAM+"""%</div>
			</div>
		</div>
			<h5 class="w3-border" >Total RAM :"""+totRAM+""" GB</h5>
			<h5 class="w3-border" >Total used :"""+usedRAM+""" GB</h5>
			<h5 class="w3-border" >Total free :"""+freeRAM+""" GB</h5>
		<button class="w3-btn w3-dark-grey w3-right " onclick="mov2()">Refresh</button>
		</div> 
	</div>



<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
</body>
</html>"""




