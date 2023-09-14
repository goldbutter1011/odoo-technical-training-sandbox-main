from odoo import fields,models

class Wear_Time(models.Model):
    _name = "optic.duration"
    _description = "Durée de port"

    name = fields.Char('Durée de port', required=True)