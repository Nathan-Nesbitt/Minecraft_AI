require.config({
    paths: {
        'vs': 'https://unpkg.com/monaco-editor@latest/min/vs'
    }
});
window.MonacoEnvironment = {
    getWorkerUrl: () => proxy
};
let proxy = URL.createObjectURL(new Blob([`
self.MonacoEnvironment = {
    baseUrl: 'https://unpkg.com/monaco-editor@latest/min/'
};
importScripts('https://unpkg.com/monaco-editor@latest/min/vs/base/worker/workerMain.js');
`], {
    type: 'text/javascript'
}));

var editor;

require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('containerMona'), {
        value: 
`var minecraft_api = new MinecraftAPIClient();

new Command(minecraft_api, "Say", ["Hello", "Friend"]);


/* Minecraft Learns Example */

// Load in minecraft model using foo.csv created before //
var args = {
    connection: minecraft_api, 
    file_name: "block_broken.csv", 
    model_type: "decision_tree_regression", 
    response_variables: ["FeetPosY", "Biome"],
    features: ["Block"]
}
var minecraft_learns = new MinecraftLearns(args);

// Create a callback function that makes a prediction based on the game data //
var callback_function_3 = function(data) {
    minecraft_learns.predict(data, ["diamond_ore"])
    .then(
        // Then use the response to move in that direction //
        result => {
            console.log("DATA FROM GAME", result.body.prediction)
            new Command(minecraft_api, "Say", ["to mine this resource go", result.body.prediction]);
        }			
    )
}

// Function that cleans the data, then trains it on the previously defined params //
minecraft_learns.process_data()
    .then(minecraft_learns.train())
    .then(
        // Then we create an event handler for the game event //
        new EventHandler(minecraft_api, "PlayerTravelled", callback_function_3)
    )`,
        language: 'javascript',
        theme: 'vs-dark'
    });
});

document.getElementById("run").addEventListener("click", (event) => {

    // obtain the script from the editor    
    var code =
        `
        // This sets the local libraries //
        EventHandler = window.EventHandler;
        Command = window.Command;
        MinecraftLearns = window.MinecraftLearns;
        DataStore = window.DataStore;
        MinecraftAPIClient = window.MinecraftAPIClient

        console.log("Command");
        `+
        editor.getValue()
    // reset the output
    document.getElementById("output").innerHTML = "";

    // Override the console.log() so it prints to the command line //
    console.log = function(output) {
        document.getElementById("console").innerHTML += ("<p> > " + output + "</p>");
    }

    // We evaluate the code //
    new Function(code)();
});

window.onresize = function (){
    editor.layout();
};

// function setSize(w, h) {
//   container.style.width = w + 'px';
//   container.style.height = h + 'px';

//   // A. When the dimension is not specified explicitly, 
//   // the editor will scan the container for the container's 
//   // new size, causing a forced layout, which is possibly undersirable
//   editor.layout();

//   // B. The editor does not need to scan the container, 
//   // avoiding a forced layout
//   editor.layout({ width: w, height: h});
// }
