# bPharma_/__manifest__.py
{
    'name': 'b-Pharmacy Management',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Gestion des médicaments en pharmacie',
    'description': """
Module pour gérer les médicaments, leurs enregistrements et stocks dans une pharmacie.
    """,
    'author': 'Adlen',
    'website': 'https://votre-site-web.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pharmacy_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
