{
    'name': 'Citix Booking',
    'version': '17.0.0.0.0',
    'description': 'Modulo de reservas para servicios de turismo',
    'summary': 'Modulo de reservas',
    'author': 'Jesus Lazo Quevedo',
    'license': 'LGPL-3',
    'category': 'Others',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/booking_demo.xml',
        'views/booking_views.xml',
        'views/booking_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'citix_booking/static/src/css/booking_widget.css',
            'citix_booking/static/src/components/*.js',
            'citix_booking/static/src/components/*.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}