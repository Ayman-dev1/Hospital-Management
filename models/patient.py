from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    note = fields.Text(string='Notes')
    examination_date = fields.Date(string='Examination Date', compute='_compute_examination_date', store=True)
    department_id = fields.Many2one('department', string='Department')
    doctor_id = fields.Many2one('doctor', string='Doctor')
    state = fields.Selection(
        [('after', 'After'), ('examination', 'Examination'), ('done', 'Done')],
        default='after'
    )

    @api.depends('state')
    def _compute_examination_date(self):
        for record in self:
            if record.state == 'examination':
                record.examination_date = fields.Date.today()

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            return {'domain': {'doctor_id': [('department_id', '=', self.department_id.id)]}}
        else:
            self.doctor_id = False
            return {'domain': {'doctor_id': [('id', '=', False)]}}

    def action_after(self):
        self.state = 'after'

    def action_patient_examination(self):
        action = self.env.ref('odoo_hos.action_patient_examination').read()[0]
        return action

    def action_examination(self):
        self.state = 'examination'

    def action_done(self):
        self.state = 'done'


