from odoo import models, fields


class Patient(models.Model):
    _name = 'patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    note = fields.Text(string='Notes')
