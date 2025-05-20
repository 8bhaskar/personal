document.addEventListener('DOMContentLoaded', function() {
    // Loading animation
    const loader = document.querySelector('.loading');
    if (loader) {
        setTimeout(() => {
            loader.remove();
        }, 1500);
    }

    // Scroll reveal animation
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Initial check

    // Video Intro Handling
    const videoIntro = document.getElementById('videoIntro');
    const introVideo = document.getElementById('introVideo');
    
    if (introVideo) {
        // Hide video intro after video ends
        introVideo.addEventListener('ended', function() {
            videoIntro.classList.add('hidden');
            document.body.style.overflow = 'auto';
        });

        // Hide video intro after 5 seconds if video doesn't end
        setTimeout(() => {
            if (!videoIntro.classList.contains('hidden')) {
                videoIntro.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        }, 5000);
    }

    // Navbar Scroll Behavior
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            navbar.classList.remove('hide');
            return;
        }
        
        if (currentScroll > lastScroll && !navbar.classList.contains('hide')) {
            // Scrolling down
            navbar.classList.add('hide');
        } else if (currentScroll < lastScroll && navbar.classList.contains('hide')) {
            // Scrolling up
            navbar.classList.remove('hide');
        }
        
        lastScroll = currentScroll;
    });

    // Initialize AOS
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add active class to current navigation item
    const currentLocation = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });

    // Project card hover effect
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
}); 