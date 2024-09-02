from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')
    patient_ids = fields.One2many('patient', 'doctor_id', string='Patients')
    nurse_ids = fields.Many2many('nurse', string='Nurses')
