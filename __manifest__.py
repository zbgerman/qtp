# -*- coding: utf-8 -*-
{
    'name': "Qtp",

    'summary': """
        Que tengo pendiente """,

    'description': """
        Que tengo pendiente para crear las pendientes y actividades
    """,

    'author': "ZB German",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/qtp_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/qtp.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.gif'],
     #Indicamos que es una aplicacion
    'application': True,
}
