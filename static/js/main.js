document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert:not(.alert-permanent)');
    
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.classList.add('fade');
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 5000);
    });
    
    // Add animation classes on scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animatedElements.length > 0) {
        const checkScroll = function() {
            animatedElements.forEach(element => {
                const elementPosition = element.getBoundingClientRect().top;
                const windowHeight = window.innerHeight;
                
                if (elementPosition < windowHeight - 100) {
                    const animationClass = element.dataset.animation || 'fade-in';
                    element.classList.add(animationClass);
                }
            });
        };
        
        window.addEventListener('scroll', checkScroll);
        // Initial check
        checkScroll();
    }
    
    // Form validation
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let valid = true;
            
            // Simple client-side validation
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const subject = document.getElementById('subject');
            const message = document.getElementById('message');
            
            // Clear previous error states
            document.querySelectorAll('.is-invalid').forEach(el => {
                el.classList.remove('is-invalid');
            });
            
            // Validate name
            if (!name.value || name.value.trim().length < 2) {
                name.classList.add('is-invalid');
                valid = false;
            }
            
            // Validate email
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!email.value || !emailRegex.test(email.value)) {
                email.classList.add('is-invalid');
                valid = false;
            }
            
            // Validate subject
            if (!subject.value || subject.value.trim().length < 3) {
                subject.classList.add('is-invalid');
                valid = false;
            }
            
            // Validate message
            if (!message.value || message.value.trim().length < 10) {
                message.classList.add('is-invalid');
                valid = false;
            }
            
            // Proceed with form submission if valid
            if (!valid) {
                e.preventDefault();
            }
        });
    }
});
