from odoo import models, fields


class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    doctor_id = fields.Many2one('doctor', string="Doctor")
    nurse_id = fields.Many2one('nurse', string="nurse")
