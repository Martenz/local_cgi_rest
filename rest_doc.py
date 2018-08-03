#!/usr/bin/env python

print """Content-type: text/html

<html><head><title>Local Rest Services</title></head><body>

<h1>Local Rest Services</h1>
<hr></hr>
<h2>Doc</h2>
<dl>
   <dt><b>Edit Server PORT (default: 8888)</b></dt>
       <dl>Edit server.py change PORT  variable (line </dl>
   <dt><b>Edit Database Connection</b></dt>
       <dl>Edit rest.py
               <p>DBNAME = 'natural_earth2'</p> 
<p>HOST = 'localhost'</p> 
<p>USER = 'user'</p> 
<p>PASSWORD = 'user!'</p> 
       </dl>
</dl>
<hr></hr>

<pre>Call example: <h1><a href='http://localhost:8888/rest.py?type=tab&schema=public&obj=ne_10m_admin_0_countries&params=' target='_blank'>Link</a></h1></pre>
eg: "http://localhost:8888/rest.py?type=tab&schema=public&obj=ne_10m_admin_0_countries&params="

<p>where </p> 
<p><b>type=</b> can be 'tab' (for tables and views calls) or 'fun' (to call functions)</p> 
<p><b>schema=</b> Database schema name</p> 
<p><b>obj=</b> Table or View or Function name</p> 
<p><b>params=</b> series of parameters, used only with <b>type=fun</b>  </p>
<dt> eg. params=(param1:value1, param2:value2)</dt> 
<p>Note: when calling tables or views leave <b>params=</b></p>


</body></html>"""