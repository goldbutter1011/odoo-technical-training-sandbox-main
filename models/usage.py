from odoo import fields,models

class Utilistaion(models.Model):
    _name = "optic.usage"
    _description = "Utilisation"

    name = fields.Char('Utilisation',required=True)