# Minecraft_AI
An in game AI implementation for Minecraft Education

## Design

### Broker
Has the following attributes:
- `models`: A dictionary of model type objects. This will allow for processes to run dynamically between the front and backend by keeping track of them using a UUID.  

- `storage`: A Minecraft_Store object. 

Has the following methods:
- `establish_connection`: Start the connection with the client side and listen in for incoming commands that are being sent over.

- `response`: Handles the commands sent from the client by converting the json object into a dictionary.

- `targetProcessId`: Handles the dictionary and extracts the information from the header and sends it over to `store` of `minecraft_learns`.

- `message_sent_back`: Handles the message that will be sent back to the front end, stating which specific message was successful or failed in being processed by the backend.

- `store`: Calls on the Store class to store the command with the game data into the clients local computer.

- `minecraft_learns`: Calls on the Minecraft_Learns class to manipulate the data in the command to produce machine learning models.

- `add_model`: Based on the UUID sent from the user this method adds a model type object to the `models` dictionary.

### Minecraft_Store
Has the following attributes:
- `files`:

Has the following methods:
- `store_filesystem`:
- `add_file`:

### Data
Has the following attributes:
- `location`:
- `filename`:

Has the following methods:
- `save_data`:
- `save_observation`:
- `add_observation`:
- `delete_data`:
- `absolute_path`:
- `rename_file`:

### Model
Has the following attributes:
- `model`:

Has the following methods:
- `pick_model`:
- `set_parameters`:
- `process_data`:
- `train_model`:
- `predict`:
- `game_response`:
- `plot`:
- `load_model`:

### Message Command

The json format sent from the client side to the broker.

```py
message = {
	    "header": {
			"UUID": "<XXXX....>",
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
- `UUID`: An ID to identify the specific messages being pass between the interfaces.
- `targetProcess`: Where the command needs to be sent to either Storage of MinecraftLearns for further processing.
- `fileName`: The file in which the game data is to be stored or used to make machine learning models.
- `modelFunction`: The model (function) that the AI will call on.

From the body:
-  `data`: Data that was retrieved from Minecraft Education.