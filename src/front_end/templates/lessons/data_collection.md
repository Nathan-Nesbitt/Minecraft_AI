# Gather Data

## Overview
### Collect Data

We are looking to pull in data from the game for the block broken event. Whenever this
happens in the game, we want to save the information relating to that event, such as the type of
block that was broken and where it was broken.

## Model Description

In this lesson we need to both collect data and save it to your computer. We also need to collect as
many events as we desire, until the connection is closed.

## Graph 
![We listen for events and save them once they occur.](../static/includes/data_store.png)

## Lesson
### Connect to Game
First we create a connection to the game. Click "Create storage" to see the next step
```
// Create connection to game and back end //
var minecraft_api = new MinecraftAPIClient();
// tell the user to break a block
new Command(minecraft_api, "Say", ["Break", "a", "block"]);
```

### Create storage
We need to make something that will store the data that we collect to a location.

Click "Save Data" to see the next step.

```
// set up the storage
var storage = new DataStore(minecraft_api, "data_collection_lesson.jsonl");
```

### Save Data
We create an a function that we call whenever we want to save the data.
This allows us to save as many events as we want.

Click "Handle event" for the next step.

```
// Callback function that handles game data and saves it to the second file //
var store_data_function = function(game_data) {
    storage.store_value(game_data)
        .then((result) => {
            console.log("Successful insertion into back end", result)
        }).catch(err => {
            // if there is a problem, log it
            console.log("Error submitting data to back end.", err);
        });
}
```

### Handle event
Finally we can handle the event occuring and save the data from the game.

Fill in the event as "BlockBroken" and click "RUN" to execute the model

```
var event_name = ""
new EventHandler(minecraft_api, event_name, store_data_function)
```
