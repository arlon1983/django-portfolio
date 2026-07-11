from django.shortcuts import render
from .forms import ContactForm
from .models import Project, Service

DEFAULT_SERVICES = [
    {'icon': '📊', 'title': 'CRM Systems', 'description': 'Lead pipelines, client history, and follow-up automation built around how your sales team actually works.'},
    {'icon': '📦', 'title': 'Inventory & Stock', 'description': 'Real-time stock tracking, reorder alerts, and multi-location inventory control.'},
    {'icon': '📅', 'title': 'Booking & Scheduling', 'description': 'Appointment calendars, availability rules, and automated confirmations.'},
    {'icon': '🛡️', 'title': 'Insurance Platforms', 'description': 'Policy management, quoting, claims tracking, and client portals.'},
    {'icon': '⚙️', 'title': 'Management Systems', 'description': 'Custom back-office tools that replace spreadsheets with real workflows.'},
    {'icon': '🧾', 'title': 'Accounting Software', 'description': 'Ledgers, invoicing, expense tracking, and financial reports built for how your business actually books revenue.'},
    {'icon': '🧑‍💼', 'title': 'HRIS', 'description': 'Human Resources Information System — employee records, attendance, leave, and payroll-ready data in one place.'},
    {'icon': '🏠', 'title': 'Rental Management', 'description': 'Tenant, lease, and payment tracking with automated rent reminders and maintenance requests.'},
    {'icon': '💱', 'title': 'Forex Agent Portal', 'description': 'Rate boards, transaction logging, and agent commission tracking for currency exchange operations.'},
    {'icon': '💰', 'title': 'Pawnshop Software', 'description': 'Ticketing, collateral tracking, interest computation, and redemption/forfeiture workflows.'},
    {'icon': '🗂️', 'title': 'Electronic Filing System', 'description': 'Digital document management with indexing, version history, and searchable records — no more paper trails.'},
    {'icon': '🧮', 'title': 'POS System', 'description': 'Point-of-sale checkout with receipts, discounts, cash/card handling, and real-time sales reporting.'},
]

DEFAULT_PROJECTS = [
    {'title': 'Insurance Management System', 'summary': 'Policy management, quoting, claims tracking, and client portals for insurance agencies.', 'tech_stack': 'Django, HTMX, PostgreSQL, Alpine.js', 'url': 'https://www.track.vizioninsurance.net'},
    {'title': 'Forex Agent Portal', 'summary': 'Rate boards, transaction logging, and agent commission tracking for currency exchange operations.', 'tech_stack': 'Django, HTMX, PostgreSQL', 'url': 'https://www.rjclportal.online'},
    {'title': 'Rental Management', 'summary': 'Tenant, lease, and payment tracking with automated rent reminders and maintenance requests.', 'tech_stack': 'Django, HTMX, PostgreSQL', 'url': 'https://www.rjclportal.online'},
]

TECH_STACK = [
    'Python', 'Django', 'HTMX', 'PostgreSQL', 'Tailwind CSS', 'Alpine.js',
    'Celery', 'Docker', 'Nginx', 'Windows Server', 'NSSM', 'AI-assisted dev',
]

DASHBOARD_IMAGES = [
    {'file': 'dashboard-1.svg', 'alt': 'Dashboard overview — policies, revenue and tickets'},
    {'file': 'dashboard-2.svg', 'alt': 'Policies table with client status and renewal dates'},
    {'file': 'dashboard-3.svg', 'alt': 'Rental units grid with occupancy status'},
    {'file': 'dashboard-4.svg', 'alt': 'Monthly revenue chart'},
    {'file': 'dashboard-5.svg', 'alt': 'Recent activity log'},
]


def home(request):
    return render(request, 'portfolio/home.html', {
        'dashboard_images': DASHBOARD_IMAGES,
    })


def services(request):
    return render(request, 'portfolio/services.html', {
        'services': Service.objects.all() or DEFAULT_SERVICES,
    })


def projects(request):
    return render(request, 'portfolio/projects.html', {
        'projects': Project.objects.all() or DEFAULT_PROJECTS,
    })


def stack(request):
    return render(request, 'portfolio/stack.html', {
        'tech_stack': TECH_STACK,
    })


def contact(request):
    return render(request, 'portfolio/contact.html', {
        'form': ContactForm(),
    })


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/partials/contact_success.html', {
                'name': form.cleaned_data['name'],
            })
        return render(request, 'portfolio/partials/contact_form.html', {'form': form})
    return render(request, 'portfolio/partials/contact_form.html', {'form': ContactForm()})
