from odoo import fields,models

class Packaging(models.Model):
    _name = "optic.packaging"
    _description = "Packagin of smoething"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Packaging est déjà en données"),
    ]
    name = fields.Char('Packaging',required=True)