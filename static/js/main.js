const root = document.documentElement;
const header = document.getElementById('site-header');
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');
const themeToggle = document.getElementById('theme-toggle');

const savedTheme = localStorage.getItem('portfolio-theme');
if (savedTheme) root.dataset.theme = savedTheme;

themeToggle?.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    localStorage.setItem('portfolio-theme', next);
});

navToggle?.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
});

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks?.classList.remove('open');
        navToggle?.setAttribute('aria-expanded', 'false');
    });
});

window.addEventListener('scroll', () => {
    header?.classList.toggle('scrolled', window.scrollY > 30);
});

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        const skillFill = entry.target.querySelector('.skill-fill');
        if (skillFill) skillFill.style.width = `${skillFill.dataset.level}%`;
        revealObserver.unobserve(entry.target);
    });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

document.querySelectorAll('.skill-card').forEach(card => {
    const fill = card.querySelector('.skill-fill');
    if (fill && card.classList.contains('visible')) fill.style.width = `${fill.dataset.level}%`;
});
