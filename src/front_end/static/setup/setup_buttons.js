/**
 * Written by Nathan Nesbitt 
 */
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



window.onload = () => {
    $('[data-toggle="popover"]').popover();

    
    var lesson = []
    var code = []
    var lessons = window.lesson
    for(var key in lessons){
        lesson.push(lessons[key]["text"])
        code.push(lessons[key]["code"])
    }

    $('#questionmrk').popover('show');
    lesson_looper(lesson, code);
}