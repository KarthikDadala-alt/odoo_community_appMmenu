{
    'name': 'Custom App Dashboard',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Modern App Dashboard',
    'depends': ['web'],
    'data': [
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_app_dashboard/static/src/js/app_dashboard.js',
            'custom_app_dashboard/static/src/xml/app_dashboard.xml',
            'custom_app_dashboard/static/src/scss/app_dashboard.scss',
        ],
    },
    'installable': True,
    'application': True,
}
