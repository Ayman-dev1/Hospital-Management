from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    note = fields.Text(string='Notes')
    examination_date = fields.Date(string='Examination Date')
    department_id = fields.Many2one('department', string='Department')
    doctor_id = fields.Many2one('doctor', string='Doctor')
    state = fields.Selection(
        [('after', 'After'), ('pending', 'Pending'), ('done', 'Done')],
        default='after'
    )

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            return {'domain': {'doctor_id': [('department_id', '=', self.department_id.id)]}}
        else:
            self.doctor_id = False
            return {'domain': {'doctor_id': [('id', '=', False)]}}

    def action_after(self):
        for rec in self:
            rec.state = 'after'

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.state = 'pending'

    def action_done(self):
        for rec in self:
            print("inside Done action")
            rec.state = 'done'


