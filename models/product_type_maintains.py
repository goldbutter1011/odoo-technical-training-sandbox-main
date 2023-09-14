from odoo import fields,models

class Product_Type_Maintains(models.Model):
    _name = "optic.product.type.maintains"
    _description = "Types de produits d'entretien"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Le type existe déjà"),
    ]
    
    name = fields.Char("Type")