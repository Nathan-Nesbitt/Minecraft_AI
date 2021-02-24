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
    var previous_code = []

    var instructions = document.getElementById("questionmrk");

    previous_button.disabled = true;
    instructions.setAttribute("data-content", "Press next to continue the lesson.");

    next_button.addEventListener("click", (event) => {

        // Handle if the user has pressed beyond the size of the input //
        if(lesson_position >= lesson.length || lesson_position >= code.length) {
            return
        }

        next_button.disabled = false;
        next_button.style.color = "#252526";
        previous_button.disabled = false;
        previous_button.style.color = "#252526";
        
        // Update the instructions
        instructions.setAttribute("data-content", lesson[lesson_position]);

        // Show the popover if it isn't already shown, or refreshes if open //
        $('#questionmrk').popover('hide')
        $('#questionmrk').popover('toggle');

        // Gets the current start line
        var start_line = window.editor.getModel().getLineCount();
        // Handles the appending to the editor //
        previous_code[lesson_position] = editor.getModel().getValue()
        window.editor.getModel().setValue(previous_code[lesson_position] + code[lesson_position]);
        
        // Move to the next lesson position //
        lesson_position++;

        // Get the size of lines changed
        var end_line = window.editor.getModel().getLineCount();
        
        window.editor.deltaDecorations([], [
            {range: new window.monaco.Range(start_line, 1, end_line, 200), options: { inlineClassName: 'highlight' }},
        ])

        // Remove the highlighting once you click on the editor
        window.editor.onMouseDown(() => {
            window.editor.deltaDecorations([], [
                {range: new window.monaco.Range(start_line, 1, end_line, 200), options: { inlineClassName: 'no_highlight' }}
            ])
        });
        
        // Disable forward button if you have reached the end of the lesson //
        if(lesson_position >= lesson.length) {
            next_button.disabled = true;
            next_button.style.color = "#4c4c4c"
        }
    })

    previous_button.addEventListener("click", (event) => {

        lesson_position--;
        // Handle if the user has pressed beyond the size of the input //
        if(lesson_position <= 0) {
            previous_button.disabled = true;
            previous_button.style.color = "#4c4c4c"
            instructions.setAttribute("data-content", "Press next to continue the lesson.");
            editor.getModel().setValue("")
            $('#questionmrk').popover('hide')
            $('#questionmrk').popover('toggle');
            return;
        }
        // Remove block on forward button //
        next_button.disabled = false;
        next_button.style.color = "#252526";
        // Handles the appending to the editor //
        editor.getModel().setValue(previous_code[lesson_position]); 

        instructions.setAttribute("data-content", lesson[lesson_position - 1]);
        // Show the popover if it isn't already shown, or refreshes if open //
        $('#questionmrk').popover('hide')
        $('#questionmrk').popover('toggle');
    })
}

code = [
    `// Create connection to game and back end //
var minecraft_api = new MinecraftAPIClient();\n`,
    `var args = {
    connection: minecraft_api, 
    file_name: "block_broken.csv", 
    model_type: "decision_tree_regression", 
    response_variables: ["FeetPosY", "Biome"],
    features: ["Block"]
}\n
var minecraft_learns = new MinecraftLearns(args);\n`,
    `// Create a callback function that makes a prediction based on the game data //
var callback_function_3 = function(data) {
    minecraft_learns.predict(data, ["diamond_ore"])
    .then(
        result => {
            // Then use the response to tell the user where to do in the game //
            new Command(minecraft_api, "Say", ["to mine this resource go to Y:", result.body.prediction.FeetPosY]);
        }            
    )
}\n`,
    `// Function that cleans the data, then trains it on the previously defined params //
minecraft_learns.process_data()
\t.then(minecraft_learns.train())
\t.then(() => {
    \t// Then we create an event handler for the game event //
    \tnew EventHandler(minecraft_api, "PlayerTravelled", callback_function_3)
\t})\n`
]

lesson = [
    "First we create a connection to the game.\nClick NEXT to see the next step",
    "Then we create a new model.\nClick NEXT to see the next step",
    "We determine what we want to predict and what to do when we have the prediction.\nClick NEXT to see the next step",
    "We need to process the data and train the model before we predict.\nClick \"RUN\" to execute the model"
]

window.onload = () => {
    lesson_looper(lesson, code);
}