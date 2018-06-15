"""
webviews.py
~~~~~~~~
Holds all the website views
"""
import aiohttp_jinja2

users = [
    {
        "name": "test",
        "occupation": "IT guy",
        "skillset": "Kubernetes"
    }
]


@aiohttp_jinja2.template('home.html')
async def home_page(request):
    """Serving the main webpage showing backend data"""
    return {'home_page_active': True}


@aiohttp_jinja2.template('about.html')
async def about_page(request):
    return {'about_page_active': True, 'users': users}