# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management System',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/appointment_view.xml',
        'views/patient_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
