// This file contains JavaScript code that interacts with the Eel backend.

function greetUser() {
    eel.get_file_path('example.txt')(function(filePath) {
        console.log("File path received from Python:", filePath);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const greetButton = document.getElementById('greet-button');
    greetButton.addEventListener('click', greetUser);
});