document.addEventListener("scroll", function() {
    const sections = document.querySelectorAll('section');
    let currentSection = 'None';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        if(window.scrollY >= sectionTop - 100 && window.scrollY < sectionTop + sectionHeight - 100){
            currentSection = section.id;
        }
    })

    document.getElementById('current-section').textContent = `Current Section: ${currentSection.charAt(0).toUpperCase() + currentSection.slice(1)}`; 
});
