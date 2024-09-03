from odoo import models, fields


class Nurse(models.Model):
    _name = 'nurse'
    _description = 'Hospital Nurse'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    department_id = fields.Many2one('department', string='Department')
