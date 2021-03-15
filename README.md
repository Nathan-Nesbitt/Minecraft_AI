# Minecraft_AI
An in game AI implementation for Minecraft Education. TESTING TESTING

## Frontend Design

## Backend Design

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

- `minecraft_learns`: Calls on the `Minecraft_Learns` class to manipulate the data in the command to produce machine learning models.

- `add_model`: Based on the UUID sent from the user this method adds a model type object to the `models` dictionary.

### Minecraft_Store
Has the following attributes:
- `files`: A dictionary that stores file names and UUIDs for the files the user wants to manipulate (either store data or have it be processed through our AI, Minecraft Learns).

Has the following methods:
- `store_filesystem`: Takes in parameters that the user specified in the frontend and calls a function to store the data into a local directory.

- `add_file`: Adds a `Data` type object which resembles a file to the `files` dictionary. This will help keep track of which file is being modified.

### Data
Has the following attributes:
- `location`: A string path to the location of the directory in which the user wants to access and potentially modify.

- `filename`: A string name for the file the user wants to access and potentially modify.

Has the following methods:
- `save_observation`: Saves event data for a specific observation that is being received from the frontend through a json object.

- `add_observation`: Adds the event data for an observation that is being received from the frontend through a json object (for single event responses).  

- `delete_data`: This method deletes a data file, removes it from its directory.

- `absolute_path`: This method returns the absolute path of a file as a string.

- `rename_file`: This method renames a preexisting file.

### Model
Has the following attributes:
- `model`: A model type object that is manipulated for machine learning processing. 

Has the following methods:
- `pick_model`: This method sets the model object to the chosen model name such as linear regressions, decision tree regression, etc.

- `set_parameters`: This method sets the appropriate parameters for the specified model.

- `process_data`: This method reads in the data from a specific file and extracts the relevant information needed.

- `train_model`: This method trains the model with the data that was processed in a previous step.

- `predict`: This method predicts and returns a response on the data being inputted.

- `game_response`: This method triggers and returns a response from the Minecraft Education game.  

- `plot`: This method plots a graph for the user and saves it in a file. The name of the file in which the plot was saved is returned.

- `load_model`: This method loads a model object from a specific file location.

- `save_model`: This method saves the model object at a given file location.

### Message Command

The json format sent from the client side to the broker.

```py
message = {
	    "header": {
			"UUID": "<XXXX....>",
		    "targetProcess": "MinecraftLearns",
		    "fileName": "MyData",
			"model_type": "Linear Regression"
	    },
	    "body": {
		    "???": {

			}
	    }
}
```
From the header:
- `UUID`: An ID to identify the specific messages being pass between the interfaces.
- `targetProcess`: Where the command needs to be sent to either Storage of MinecraftLearns for further processing.
- `fileName`: The file in which the game data is to be stored or used to make machine learning models.
- `model_type`: The model (function) that the AI will call on.

From the body (`???`):
- `features`: The columns of data that we want to use for processing the data for our machine learning models.

- `features_drop`: The columns of data that we want to not included when processing data for our machine learning models.

- `function`: A keyword that determines what `Minecraft_Learns` will do, either process, train, predict, or plot the data.

- `params`: The parameters that are needed for the given model object.

- `response_variables`: The response variables needed to process the data for our machine learning models.

- `value`: The specific value we want to predict using our machine learning models.