from django.core.management.base import BaseCommand
from core.models import Education, Project, Skill


class Command(BaseCommand):
    help = 'Seed Kabindra Karki portfolio content'

    def handle(self, *args, **options):
        skills = [
            ('HTML5', 'frontend', 88, 1),
            ('CSS3', 'frontend', 85, 2),
            ('JavaScript', 'frontend', 78, 3),
            ('Python', 'backend', 86, 4),
            ('Django', 'backend', 82, 5),
            ('Django REST Framework', 'backend', 72, 6),
            ('PostgreSQL', 'database', 70, 7),
            ('Git & GitHub', 'tools', 76, 8),
            ('VS Code', 'tools', 90, 9),
        ]
        for name, category, level, order in skills:
            Skill.objects.update_or_create(
                name=name,
                defaults={'category': category, 'level': level, 'display_order': order},
            )

        projects = [
            {
                'title': 'NexusGhr Nepal',
                'short_description': 'A startup incubation and collaboration platform connecting students and entrepreneurs with teams, mentors, investors, events, and project-tracking tools.',
                'description': 'NexusGhr Nepal is an ongoing web-based startup incubation and collaboration platform created for students and entrepreneurs in Nepal. The platform is designed to help users share startup ideas, discover co-founders and team members, connect with mentors and investors, participate in startup events, and follow project progress in one place. The backend uses Django and Django REST Framework, with PostgreSQL for structured data and API-ready development.',
                'technologies': 'Python, Django, Django REST Framework, PostgreSQL, HTML5, CSS3, Bootstrap, JavaScript, Git/GitHub',
                'status': 'ongoing', 'featured': True, 'display_order': 1,
            },
            {
                'title': 'Hotel Management System',
                'short_description': 'A database-driven web application concept for managing hotel rooms, guests, reservations, and booking-related information.',
                'description': 'A full-stack hotel management project designed to organize common hotel operations in a single web application. The project combines Django backend logic with structured data handling and responsive frontend pages for tasks such as room information, guest records, and reservations.',
                'technologies': 'Python, Django, HTML5, CSS3, JavaScript, SQLite/PostgreSQL',
                'status': 'completed', 'featured': True, 'display_order': 2,
            },
            {
                'title': 'Website Cloning',
                'short_description': 'Frontend recreations of modern website layouts used to practice responsive design, navigation, spacing, and reusable UI components.',
                'description': 'A collection of website recreation exercises focused on translating visual references into clean HTML structure, modern CSS layouts, responsive behavior, and JavaScript-based interactions. These projects helped strengthen attention to detail and practical frontend implementation skills.',
                'technologies': 'HTML5, CSS3, JavaScript, Responsive Design',
                'status': 'practice', 'featured': True, 'display_order': 3,
            },
            {
                'title': '2D Mini Games Collection',
                'short_description': 'Small interactive games including Rock Paper Scissors, number guessing, and character/word challenges.',
                'description': 'A collection of beginner-friendly interactive games created to practice programming logic, conditional statements, loops, event handling, user input validation, and simple interface design. The collection includes Rock Paper Scissors, a number guessing game, and character/word-based challenges.',
                'technologies': 'Python, JavaScript, HTML5, CSS3',
                'status': 'practice', 'featured': True, 'display_order': 4,
            },
        ]
        for item in projects:
            Project.objects.update_or_create(title=item['title'], defaults=item)

        education = [
            ('Bachelor of Science in Information Technology (BSc IT)', 'Techspire College', 'Ongoing', '', 1),
            ('Secondary Level Certificate (SLC)', "Golden Gate Int'l College", '2024', '3.38', 2),
            ('Secondary Education Examination (SEE)', 'Saraswati Secondary School', '2022', '3.25', 3),
        ]
        for qualification, institution, completion, gpa, order in education:
            Education.objects.update_or_create(
                qualification=qualification,
                institution=institution,
                defaults={'completion': completion, 'gpa': gpa, 'display_order': order},
            )

        self.stdout.write(self.style.SUCCESS('Portfolio data seeded successfully.'))
