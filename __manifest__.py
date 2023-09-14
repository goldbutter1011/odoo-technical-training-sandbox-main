{
    'name': 'Optique',
    'version': '1.0',
    'author': 'Htcompass',
    'category': '',
    'summary': 'Safy Optic software',
    'description': "Safy optic gestion de stock",
    'depends':['base','product'],
    'data' : [
        'security/ir.model.access.csv',
        'views/brand_views.xml',
        'views/modeles_views.xml',
        'views/caracteristique_views.xml',
        'views/wear_time_views.xml',
        'views/usage_views.xml',
        'views/packaging_views.xml',
        'views/product_type_maintains_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/lense_mount_color.xml',
        'views/optic_view_menus.xml',
    ],
    'demo': [
    ],
    'sequence': 1,
    'application': True,
    'autoinstall': False,
    'installable': True
}