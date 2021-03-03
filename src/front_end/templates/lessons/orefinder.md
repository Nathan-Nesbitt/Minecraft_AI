# Ore Finder

## Overview
### Problem Description

We are looking for a depth. This can be any value on the number line.
Since we are looking for a value on the number line and not a group, 
this is a REGRESSION problem.

## Model Description

In this lesson we will use a Decision Tree to determine the location of a material. In order to find
the location, we will search each node to look for the value that we want.

Follow the splits in the tree for the material you want. The depth is listed below.

## Graph 
![In order to find the desired value, follow the split to the node you want.](../static/includes/decision_tree.png)

## Lesson
### Instruction 1
We need to create a connection to the game in order for code to run.

Click NEXT to see the next step
```
// Create connection to game and back end //
var minecraft_api = new MinecraftAPIClient();
```

### Instruction 2
We transform the problem into a machine learning model with predictors and responses.

Click NEXT to see the next step

```
var args = {
    connection: minecraft_api, 
    file_name: "block_broken.csv", 
    model_type: "decision_tree_regression", 
    response_variables: ["FeetPosY", "Biome"],
    features: ["Block"]
}

var minecraft_learns = new MinecraftLearns(args);

```

### Instruction 3
We determine what we want to do with the model.

Click NEXT to see the next step

```
// Create a callback function that makes a prediction based on the game data //
var callback_function_3 = function(data) {
    var resource = "diamond_ore"
    minecraft_learns.predict(data, [resource])
    .then(
        result => {
            // Then use the response to tell the user where to do in the game //
            if(data.body.properties.FeetPosY == result.body.prediction.FeetPosY)
                new Command(minecraft_api, "Say", ["Mine here to find: ", resource]);
            else
                new Command(minecraft_api, "Say", ["to mine this resource go to Y:", result.body.prediction.FeetPosY]);
        }            
    )
}
```

### Instruction 4
We process the data for training. After training, we can make predictions.

Click "RUN" to execute the model and see the effect in game!
```
// Function that cleans the data, then trains it on the previously defined params //
minecraft_learns.process_data()
    .then(minecraft_learns.train())
    .then(() => {
        // Then we create an event handler for the game event //
        new EventHandler(minecraft_api, "PlayerTravelled", callback_function_3)
    })
```
