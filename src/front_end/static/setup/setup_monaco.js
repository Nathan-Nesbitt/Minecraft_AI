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

require(['vs/editor/editor.main'], function () {
    window.monaco = monaco;
    monaco.languages.registerCompletionItemProvider('javascript', {
        provideCompletionItems: () => {
            return { 
                suggestions: [
                    {
                        label: 'MinecraftLearns',
                        kind: monaco.languages.CompletionItemKind.Class,
                        documentation: "Creates a new machine learning algorithm.",
                        insertText: 'new MinecraftLearns({\n\tconnection: minecraft_api,\n\tfile_name: "",\n\tmodel_type: "",\n\tresponse_variables: [],\n\tfeatures: []\n});',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                    },
                    {
                        label: 'Command',
                        kind: monaco.languages.CompletionItemKind.Class,
                        documentation: "A command that can be sent to Minecraft Education.",
                        insertText: 'minecraft_api.Command("Command", ["Parameters"]);',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                    },
                    {
                        label: 'MinecraftAPIClient',
                        kind: monaco.languages.CompletionItemKind.Class,
                        documentation: "Creates a new connection to both minecraft education and the backend.",
                        insertText: 'var minecraft_api = new MinecraftAPIClient();',
                        insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                    },
                    {
                        label: 'EventHandler',
                        kind: monaco.languages.CompletionItemKind.Class,
                        documentation: "Handles an in game event and calls a function when triggered.",
                        insertText: 'minecraft_api.EventHandler("event_name", callback_function);',
                    },
                    {
                        label: 'DataStore',
                        kind: monaco.languages.CompletionItemKind.Class,
                        documentation: "Object for storing in game data on the back end.",
                        insertText: 'new DataStore(minecraft_api, "filename.jsonl");',
                    },
                    {
                        label: 'callback_function',
                        kind: monaco.languages.CompletionItemKind.Function,
                        documentation: "Callback function example",
                        insertText: `var callback_function = function(data) { \
                            \n\t// Run some code based on the game event // \
                        \n}`
                    },
                    {
                        label: 'minecraft_learns_callback_function',
                        kind: monaco.languages.CompletionItemKind.Function,
                        documentation: "Callback function for minecraft learns example",
                        insertText: `var callback_function = function(data) { \
                            \n\tminecraft_learns.predict(data, ["diamond_ore"]) \
                            \n\t.then( \
                                \n\t\tresult => { \
                                    \n\t\t\t// Then do something with the prediction // \
                                    \n\t\t\tnew Command(minecraft_api, "Say", ["to mine this resource go", result.body.prediction]); \
                                \n\t\t} \
                            \n\t) \
                        \n}`
                    },
                    {
                        label: 'datastore_callback_function',
                        kind: monaco.languages.CompletionItemKind.Function,
                        documentation: "Callback function for data store example",
                        insertText: `var callback_function = function(game_data) { \
                            \n\tdatastore.store_value(game_data) \
                            \n\t.then((result) => { \
                                \n\t\tconsole.log("Successful insertion into back end", result); \
                            \n\t}).catch(err => { \
                                \n\t\tconsole.log("Error submitting data to back end.", err); \
                            \n\t}); \
                        \n}`
                    },
                ]
            }
        }
    })
    window.editor = monaco.editor.create(document.getElementById('containerMona'), {
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
        MinecraftLearns = window.MinecraftLearns;
        MinecraftAPIClient = window.MinecraftAPIClient

        `+
        window.editor.getValue()
    // reset the output
    document.getElementById("console").innerHTML = "";

    // Override the console.log() so it prints to the command line //
    console.log = function(output) {
        document.getElementById("console").innerHTML += ("<p> > " + output + "</p>");
    }
    // This routes the window errors to the same element but makes it red //
    window.onerror = function(message, url, linenumber) {
        document.getElementById("console").innerHTML += 
            ("<p style='color: red'> > ERROR: " + message + "</p>");
    }

    // We evaluate the code //
    new Function(code)();
});

window.onresize = function (){
    window.editor.layout();
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
