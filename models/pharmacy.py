from odoo import models, fields # type: ignore

class PharmacyMedicine(models.Model):
    _name = 'bpharma.medicine'
    _description = 'Médicament en pharmacie'

    registration_number = fields.Char(string='N° ENREGISTREMENT')
    code = fields.Char(string='Code')
    dci = fields.Char(string='DCI')
    brand_name = fields.Char(string='Nom de Marque')
    form_med = fields.Char(string='Forme Médicament')  # correspond à <field name="form_med"/>
    dosage = fields.Char(string='Dosage')
    packaging = fields.Char(string='Conditionnement')
    lab_holder = fields.Char(string='Laboratoire Détenteur')
    lab_holder_country = fields.Char(string='Pays du Laboratoire Détenteur')
    date_registration_init = fields.Date(string='Date d\'Enregistrement Initial')
    date_registration_final = fields.Date(string='Date d\'Enregistrement Final')
    type_medicine = fields.Char(string='Type')
    status_medicine = fields.Char(string='Statut')
    stability_duration = fields.Char(string='Durée de Stabilité')
    quantity = fields.Integer(string='Quantité')
    price = fields.Float(string='Prix')
