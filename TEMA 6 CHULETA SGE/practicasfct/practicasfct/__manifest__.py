# -*- coding: utf-8 -*-
{
    'name': "practicasfct",

    'summary': """

        Módulo para gestionar alumnos y empresas de prácticas.
        """,

    'description': """
        El modulo que vamos a hacer va a representar la
        información sobre los alumnos de un centro de FP y en que empresa están
        haciendo o han hecho las prácticas.
        Tendremos dos objetos en nuestro sistema: alumno y empresa.
    """,

    'author': "Shaila",
    'website': "http://www.shaila.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_empresa.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
