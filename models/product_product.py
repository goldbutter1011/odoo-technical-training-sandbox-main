from odoo import api,fields,models


class Product_product(models.Model):
    _inherit = "product.product"
    
    type_verre = fields.Selection(
        selection = [
            ('verre_stock','Verre de stock'),
            ('verre_commande','Verre de commande'),
        ],
        string = "Typer de verre")
   
    collection = fields.Char('Collection')
    ref_catalogue = fields.Char('Réf. Catalogue')
    
    brand_id = fields.Many2one('optic.brand',string = "Marque du produit")
    model_id = fields.Many2one('optic.modele',string = "Modèle du produit",domain = '[("marque_id","=", brand_id)]')
    usage_ids = fields.Many2many('optic.usage', string = "Utilisation")
    caracteristics_id = fields.Many2many('optic.caracteristique', string = "Autres caractérestiques")
    lense_color = fields.Many2one('optic.couleur.lentilles.monture','Couleur de lentilles de monture')

    date_experation = fields.Date()
    optimal_use_date = fields.Date()

    uv_treatment = fields.Boolean(string="Traitement UV")
    wear_time_id = fields.Many2one('optic.duration',string = "Durée du port")
    packaging = fields.Many2one('optic.packaging',string = "Packaging")
    product_type_maintain_ids = fields.Many2many('optic.product.type.maintains',string = "Types de produit d'entretien")



    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s /%s /%s" % (record.name,record.brand_id.name,record.model_id.name)
            result.append((record.id, rec_name))
        return result

   
    @api.onchange('brand_id')
    def _onchange_brand_id(self) :
        self.model_id = None


    @api.onchange('model_id')
    def _onchange_model_id(self) : 
        self.brand_id = self.model_id.marque_id