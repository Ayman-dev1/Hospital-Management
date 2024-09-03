from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')
    department_id = fields.Many2one('department', string='Department')
    nurse_id = fields.Many2one('nurse', string='Nurses')

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            return {'domain': {'nurse_id': [('department_id', '=', self.department_id.id)]}}
        else:
            self.nurse_id = False  # Clear the selected nurse if no department is selected
            return {'domain': {'nurse_id': [('id', '=', False)]}}
