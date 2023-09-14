from odoo import api,fields,models

class Modele(models.Model):
    _name = "optic.modele"
    _description = "Modele du produit"
    _sql_constraints = [
        ('Check_name','UNIQUE(name)',"Modèle en possession déjà")
    ]
    name = fields.Char('Nom de modèle',required = True)
    marque_id = fields.Many2one('optic.brand',string="Marque de modèle", required = True)
    
    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s /%s" % (record.marque_id.name,record.name)
            result.append((record.id, rec_name))
        return result
