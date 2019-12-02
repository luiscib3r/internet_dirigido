# -*- coding: utf-8 -*-
{
    'name': "internet_dirigido",

    'summary': """
        Internet Dirigido
    """,

    'description': """
        
    """,

    'author': "Luis Correa",
    'website': "https://www.soft4cuba.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/conexion.xml',
        'views/cliente.xml',
        'views/oferta.xml',
        'views/templates.xml',
        'data/stage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}