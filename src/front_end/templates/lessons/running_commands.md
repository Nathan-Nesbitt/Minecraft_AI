# Gather Data

## Overview
### Collect Data

You can write code to do actions within the game. This can be used to do more complex actions.

## Model Description

In this lesson you will write code to say text in the game. Commands can also be used for movement and placing blocks.

## Graph 
![Writing and running code can have effects in the game](../static/includes/running_commands.png)

## Lesson
### Connect to Game
First we create a connection to the game using MinecraftAPIClient. Click "Say Hello" to see the next step
```
// Create connection to game and back end //
var minecraft_api = new MinecraftAPIClient();
```

### Say Hello
We can write a command by writing the name of the command and passing in any necessary arguements specifying the details of the command.

Click "Choose Arguments" to see the next step.

```
// say hello
minecraftAPI.Say(["Hello"]);

// say "how are you"
// we need to write each word in a list using []
minecraftAPI.Say(["How", "are", "you?"]);
```

### Choose Arguments
When deciding what kind of arguments to give, we can write code to define what we want to say. Add a list of words you want to say, then click "Callback Functions" for the next step.

```
// Add the words you want to say
var words = [""];
minecraftAPI.Say(words);
```

### Callback Functions
We can use a callback function to execute other code chunks when the command is run. Click "RUN" to execute the commands

```
// create a callback function to say the command has been executed
var callback_function () {
    minecraftAPI.Say(["callback", "function", "used"]);
}
minecraftAPI.Say(["callback", "function", "used"], callback_function);
```
