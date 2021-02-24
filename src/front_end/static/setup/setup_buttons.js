/**
 * Written by Nathan Nesbitt 
 */
$(document).ready(function(){
    $('[data-toggle="popover"]').popover();

});
/**
 * Handles the appending of new lessons
 * @param {Array} lesson Lesson text
 * @param {Array} code Lesson code
 */
var lesson_looper = function(lesson, code) {

    var lesson_position = 0;
    var next_button = document.getElementById("nextbutton");
    var previous_button = document.getElementById("previousbutton");
    var previous_code = window.editor.getModel().getValue();

    next_button.addEventListener("click", (event) => {
        // Handle if the user has pressed beyond the size of the input //
        if(lesson_position >= lesson.length || lesson_position >= code.length)
            return;

        // Gets the current start line
        var start_line = window.editor.getModel().getLineCount();
        // Handles the appending to the editor //
        previous_code = editor.getModel().getValue();
        window.editor.getModel().setValue(previous_code + code[lesson_position]);
        
        // Get the size of lines changed
        var end_line = window.editor.getModel().getLineCount();

        console.log(start_line, end_line)
        
        window.editor.deltaDecorations([], [
            {range: new window.monaco.Range(start_line, 1, end_line, 200), options: { inlineClassName: 'highlight' }},
        ])

        // Remove the highlighting once you click on the editor
        window.editor.onMouseDown(() => {
            window.editor.deltaDecorations([], [
                {range: new window.monaco.Range(start_line, 1, end_line, 200), options: { inlineClassName: 'no_highlight' }}
            ])
        });
        // Once the lesson area is implemented simply append to it //
        lesson_position++;
    })

    previous_button.addEventListener("click", (event) => {
        // Handle if the user has pressed beyond the size of the input //
        if(lesson_position <= 0)
            return;
        // Handles the appending to the editor //
        editor.getModel().setValue(previous_code); 
        
        // Once the lesson area is implemented simply append to it //

        lesson_position--;
    })
}

code = [
    '\nvar minecraft_api = new MinecraftAPIClient();\n',
    'new Command(minecraft_api, "Say", ["Hello", "Friend"]);\n',
    `var args = {
        connection: minecraft_api, 
        file_name: "block_broken.csv", 
        model_type: "decision_tree_regression", 
        response_variables: ["FeetPosY", "Biome"],
        features: ["Block"]
    }
    var minecraft_learns = new MinecraftLearns(args);`
]

lesson = [
    "First we create a connection to the game.",
    "Then we can create a command to be sent to the game.",
    "Then we create a new MinecraftLearns model."
]

window.onload = () => {
    lesson_looper(lesson, code);
}


/*
command_button.addEventListener("click", (e)=> {
    var command_select = document.getElementById("command");
    var command_arg = document.getElementById("command-arguement");

    // verify that the arguement is filled
    if(command_arg.value == ""){
        window.alert("Error - Please input an argument");
        return;
    }
    
    // create text to inject
    text = "api.add_message(new Command(\""+command_select.value+"\", \""+command_arg.value+"\"));\n";

    // inject text at current cursor position
    editor.trigger('keyboard', 'type', {text: text});
    console.log(text);

});

event_button.addEventListener("click", (e)=> {
    var event_select = document.getElementById("event-name");
    var event_arg = document.getElementById("event-arguement");

    // verify that the arguement is filled
    if(event_arg.value == ""){
        window.alert("Error - Please input an argument");
        return;
    }
    
    // create text to inject
    text = "api.add_message(new EventHandler(\""+event_select.value+"\", "+event_arg.value+"));\n";
            
    // inject text at current cursor position
    editor.trigger('keyboard', 'type', {text: text});
    console.log(text);

});

var help_button = document.getElementById("help");
help_button.addEventListener("click", (e) =>{
    console.log("help wanted");

    var overlay = document.getElementById("overlay");
    overlay.style.display = "block";
    overlay.addEventListener("click", (e)=>{
        overlay.style.display = "none";
    });
});
*/