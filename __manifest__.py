# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'sequence': -100,
    'author': "Ayman Elwan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Healthcare',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/patient_examination_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/nurse_view.xml',
        'views/department_view.xml',
        'views/sale_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
