# TTN-Data-Connector
These python files collect data from sensors that are registered on The Things Network (TTN) and save it in a database.

## How to execute
<p>Let's clone the respository first...</p>

```git clone https://github.com/itguy19/TTN-Data-Connector.git```
<p>... and use python3 to start FetchData.py.</p>

```python3 FetchData.py```

<p>If everything is setup correctly, this ouput should appear in the terminal:</p>

![image](https://user-images.githubusercontent.com/125930481/235115079-3e3efc33-ee2f-42d8-861f-7ea2b9c4b09a.png)

<p>The 200 status code says that the Linux server could be contacted and all sensor names were retrieved. The flags with the values 0 show, that a connection with the TTN (The Things Network) has been successfully established.</p>
