from odoo import fields,models

class lense_color_Monture(models.Model):
    _name = "optic.couleur.lentilles.monture"
    _description = "Couleurs De Lentilles Monture"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Couleur existe déjà"),
    ]

    name = fields.Char('Couleur')