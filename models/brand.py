from odoo import api,fields,models

class Brand(models.Model):
    _name = "optic.brand"
    _description = "Marque du produit"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Marque est déjà en liste"),
    ]
    
    name = fields.Char('Nom de marque', required = True, index = True)
    modele_ids = fields.One2many('optic.modele','marque_id',string="Modèles disponibles")