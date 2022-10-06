# -*- coding: utf-8 -*-
{
    "name": "Chatter Position",
    "summary": "Chatter Position",
    "version": "14.0.1.0.3",
    'author': "Odoo Being, Odoo Community Association (OCA)",
    'website': "https://www.odoobeing.com",
    'license': "LGPL-3",
    "category": "Extra Tools",
    'images': ['static/description/images/ob_chatter_position.png'],
    'support': 'odoobeing@gmail.com',
    "depends": ["web", "mail"],
    "data": [
        "views/res_users.xml",
        "views/web.xml",
        "views/assets.xml",
    ],
    'qweb': [
        'static/src/xml/form_buttons.xml',
    ],
    'installable': True,
    'auto_install': False,
}
