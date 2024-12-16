// Check for saved theme preference in localStorage
const darkModeToggle = document.getElementById('darkModeToggle');
const currentTheme = localStorage.getItem('theme') || 'light';

if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
    darkModeToggle.checked = true;
} else {
    document.body.classList.add('light-mode');
    darkModeToggle.checked = false;
}

// Event listener for theme toggle
darkModeToggle.addEventListener('change', () => {
    if (darkModeToggle.checked) {
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-mode');
        localStorage.setItem('theme', 'dark');
    } else {
        document.body.classList.add('light-mode');
        document.body.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
    }
});
