// Simple JavaScript for interactions
document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // File upload preview
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                console.log('Selected file:', fileName);
            }
        });
    }
});
// Enhanced futuristic animations
document.addEventListener('DOMContentLoaded', function() {
    
    // Floating grid animation
    const grid = document.querySelector('.dark-theme::before');
    if (grid) {
        let position = 0;
        setInterval(() => {
            position = (position + 0.5) % 50;
            grid.style.transform = `translateY(${position}px)`;
        }, 50);
    }
    
    // Glowing effect for feature cards on hover
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 0 30px rgba(0, 212, 255, 0.4)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
        });
    });
    
    // Auto-dismiss alerts
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            if (alert) {
                let bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        });
    }, 5000);
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Typing effect for hero text (optional)
    const heroText = "Welcome to the Future of Learning";
    let i = 0;
    const speed = 50;
    
    function typeWriter() {
        if (i < heroText.length) {
            document.getElementById("hero-text").innerHTML += heroText.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }
    
    // Start typing effect if element exists
    if (document.getElementById("hero-text")) {
        typeWriter();
    }
});