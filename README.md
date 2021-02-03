# Minecraft_AI
An in game AI implementation for Minecraft Education

## Design

### Broker
Has the following methods:

- `establish_connection`: Start the connection with the client side and listen in for incoming commands that are being sent over.

- `response`: Handles the commands sent from the client by converting the json object into a dictionary.

- `targetProcessId`: Handles the dictionary and extracts the information from the header and sends it over to `store` of `minecraft_learns`.

- `store`: Calls on the Store class to store the command with the game data into the clients local computer.

- `minecraft_learns`: Calls on the Minecraft_Learns class to manipulate the data in the command to produce machine learning models.

### Store
Has the following methods:

-``

### Data
Has the following methods:

- ``

### Message Command

The json format sent from the client side to the broker.

```py
message = {
	    "header": {
		    "targetProcess": "MinecraftLearns",
		    "fileName": "MyData",
			"modelFunction": "Linear Regression"
	    },
	    "body": {
		    "data": {

			}
	    }
}
```
From the header:
- `targetProcess`: Where the command needs to be sent to either Storage of MinecraftLearns for further processing.
- `fileName`: The file in which the game data is to be stored or used to make machine learning models.
- `modelFunction`: The model (function) that the AI will call on.

From the body:
-  `data`: Data that was retrieved from Minecraft Education.