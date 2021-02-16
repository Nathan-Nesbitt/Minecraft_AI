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
`// Create a minecraftAPI connection
var minecraft_api = new MinecraftAPIClient();

// Create a new command to the game
new Command(minecraft_api, "Say", ["Hello", "Friend"]);

// Creates 2 separate datastore connections for saving backend data //
var datastore = new DataStore(minecraft_api, "foo.csv")
var datastore_2 = new DataStore(minecraft_api, "foo_2.csv")

// Callback function that handles game data and saves it to the first file //
var callback_function = function(game_data) {
    datastore.store_value(game_data)
        .then((result) => {
            console.log("Successful insertion into back end", result)
        }).catch(err => {
            console.log("Error submitting data to back end.", err);
        });
}

// Callback function that handles game data and saves it to the second file //
var callback_function_2 = function(game_data) {
    datastore_2.store_value(game_data)
        .then((result) => {
            console.log("Successful insertion into back end", result)
        }).catch(err => {
            console.log("Error submitting data to back end.", err);
        });
}

// Creates two new event handlers for blocks being broken and placed //
new EventHandler(minecraft_api, "BlockBroken", callback_function)
new EventHandler(minecraft_api, "BlockPlaced", callback_function_2)

// Opens a connection to the back end //
minecraft_api.open_backend_connection();
// Opens the connection to the game //
minecraft_api.start()
        `,
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