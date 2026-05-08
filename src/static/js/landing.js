// ===== Navbar Scroll Effect =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});

// ===== Mobile Menu =====
const menuBtn = document.getElementById('menu-btn');
const closeMenuBtn = document.getElementById('close-menu');
const mobileMenu = document.getElementById('mobile-menu');
const menuOverlay = document.getElementById('menu-overlay');

function openMenu() {
    mobileMenu.classList.add('active');
    menuOverlay.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    mobileMenu.classList.remove('active');
    menuOverlay.classList.add('hidden');
    document.body.style.overflow = '';
}

menuBtn.addEventListener('click', openMenu);
closeMenuBtn.addEventListener('click', closeMenu);
menuOverlay.addEventListener('click', closeMenu);

// Close menu on link click
document.querySelectorAll('#mobile-menu a').forEach(link => {
    link.addEventListener('click', closeMenu);
});

// ===== Search Tab Switching =====
function switchTab(btn) {
    document.querySelectorAll('.search-tab').forEach(tab => {
        tab.classList.remove('active');
        tab.classList.add('bg-white/5', 'text-white/70');
    });
    btn.classList.add('active');
    btn.classList.remove('bg-white/5', 'text-white/70');
}

// ===== Property Filter =====
function filterProperties(btn, type) {
    document.querySelectorAll('.filter-btn').forEach(b => {
        b.classList.remove('active', 'bg-blue-500', 'text-white');
        b.classList.add('bg-white', 'text-slate-600', 'border', 'border-slate-200');
    });
    btn.classList.add('active', 'bg-blue-500', 'text-white');
    btn.classList.remove('bg-white', 'text-slate-600', 'border', 'border-slate-200');

    document.querySelectorAll('.property-card').forEach(card => {
        const cardType = card.getAttribute('data-type');
        if (type === 'all' || cardType.includes(type)) {
            card.style.display = 'block';
            card.style.animation = 'fadeIn 0.5s ease forwards';
        } else {
            card.style.display = 'none';
        }
    });
}

// ===== Heart Button Toggle =====
document.querySelectorAll('.fa-heart').forEach(heart => {
    heart.parentElement.addEventListener('click', function (e) {
        e.preventDefault();
        const icon = this.querySelector('i');
        if (icon.classList.contains('text-red-500')) {
            icon.classList.remove('text-red-500');
            icon.classList.add('text-slate-400');
            this.classList.remove('bg-red-50');
            this.classList.add('bg-white/90');
        } else {
            icon.classList.remove('text-slate-400');
            icon.classList.add('text-red-500');
            this.classList.remove('bg-white/90');
            this.classList.add('bg-red-50');
        }
    });
});

// ===== Counter Animation =====
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.ceil(current).toLocaleString() + '+';
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString() + '+';
            }
        };
        updateCounter();
    });
}

// ===== Scroll Animations =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('visible');
            }, index * 100);
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in-up').forEach(el => {
    observer.observe(el);
});

// Stats counter trigger
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const statsSection = document.querySelector('.stat-number');
if (statsSection) {
    statsObserver.observe(statsSection.parentElement.parentElement);
}

// ===== Back to Top Button =====
const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
        backToTop.classList.remove('opacity-0', 'invisible');
        backToTop.classList.add('opacity-100', 'visible');
    } else {
        backToTop.classList.add('opacity-0', 'invisible');
        backToTop.classList.remove('opacity-100', 'visible');
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ===== Smooth Scroll for Anchor Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ===== Form Submission (Demo) =====
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        // Show a simple success message
        const btn = this.querySelector('button[type="submit"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-check mr-2"></i> Sent Successfully!';
        btn.classList.add('bg-green-500');
        btn.classList.remove('from-blue-500', 'to-indigo-600');

        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.classList.remove('bg-green-500');
            btn.classList.add('from-blue-500', 'to-indigo-600');
            this.reset();
        }, 3000);
    });
});
