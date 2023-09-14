from odoo import fields,models
class Caracteristique(models.Model):
    _name = "optic.caracteristique"
    _description = "Caracteristique"
    
    name = fields.Char("Caractéristique", required=True)


