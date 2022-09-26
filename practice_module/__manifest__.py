# -*- coding: utf-8 -*-

{
    'name': 'Practice Module',
    'version': '1.1',
    'sequence': '1',
    'category': 'Training ',
    'summary': 'Learning Odoo',
    'description': 'This is the practice module on working with odoo ',
    'depends': ["base"],
    'data': [
        "security/ir.model.access.csv",
        "views/department_subject_view.xml",
        "views/student_view.xml",
        "views/menu_view.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
