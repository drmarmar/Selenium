# Selenium Scripts

## Usage
Execute script with URL, SessionID, and file arguments. The SessionID is obtained from the Selenium Node web interface after you create a session. 

"Take a screenshot" within the Selenium Node web interface to view the file or folder you specified in the arguments. 

```
python3 node-fileread.py -u 'http://localhost:4444/wd/hub' -s 872de14392f18a99a2298c4a1d732743 -f '/etc/passwd' 
```
