# -*- coding: utf-8 -*-
{
    'name': "Helpdesk ticket without being logged",
    # odoo_helpdesk_ticket_no_user
    'summary': """
        Allows to create a ticket without being logged""",

    'description': """
        Allows to create a ticket without being logged
    """,

    'author': "Miguel Hatrick",
    'website': "http://www.dacosys.com",

    'category': 'Helpdesk',
    'version': '12.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk_mgmt'],

    # always loaded
    'data': [
        'views/helpdesk_ticket_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
