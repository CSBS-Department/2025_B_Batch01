// script.js
document.getElementById('submitForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Start progress bar animation
    var progressBar = document.getElementById('progressBar');
    progressBar.innerHTML = '<div class="progress"></div>';
    var progress = 0;
    var interval = setInterval(function() {
        progress += 1;
        if (progress >= 100) {
            clearInterval(interval);
            // Submit form data using AJAX or fetch
            // Upon success, redirect to the result page
            window.location.href = 'result.html';
        }
        document.querySelector('.progress').style.width = progress + '%';
    }, 50);
});
