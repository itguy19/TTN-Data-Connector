# TTN-Data-Connector
These python files collect data from all the sensors that are registered on The Things Network (TTN) and save it in a MySQL database on a Linux server. The script connects to the database via an API on the server.

## How to execute
<p>Let's clone the respository first.</p>

```git clone https://github.com/itguy19/TTN-Data-Connector.git```

<p>Create a new directory called "data" in the cloned repository and create three new files with these names: api_key, app_id nad iot_api_key.</p>

```mkdir data```

```touch api_key```

```touch app_id```

```touch iot_api_key```

<p>The API key file should contain the API key for the TTN application (See how you can create a new application: )</p>

<p>... and use python3 to start FetchData.py.</p>

```python3 FetchData.py```

<p>If everything is setup correctly, this ouput should appear in the terminal:</p>

![image](https://user-images.githubusercontent.com/125930481/235115079-3e3efc33-ee2f-42d8-861f-7ea2b9c4b09a.png)

<p>The 200 status code says that the Linux server could be contacted and all sensor names were retrieved. The flags with the values 0 show, that a connection with the TTN (The Things Network) has been successfully established.</p>
