from odoo import models,fields


class ModuleName(models.Model):
    _inherit = 'product.template'

    nature_article = fields.Selection(
        selection = [
            ('monture','Monture'),
            ('verre','Verre'),
            ('lentilles','Lentille de contact'),
            ('accessoire','Accessoire')
            ],
        string = "Nature d'article",
        )