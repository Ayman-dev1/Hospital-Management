from odoo import models, fields, api


class PatientExamination(models.TransientModel):
    _name = 'patient.examination'
    _description = 'Examination Wizard'

    examination_date = fields.Date(string='Examination Date', required=True, default=fields.Date.context_today)
    department_id = fields.Many2one('department', string='Department', required=True)
    doctor_id = fields.Many2one('doctor', string='Doctor', required=True)

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            return {'domain': {'doctor_id': [('department_id', '=', self.department_id.id)]}}
        else:
            self.doctor_id = False
            return {'domain': {'doctor_id': []}}

    def action_apply(self):
        patient_id = self.env.context.get('active_id')
        patient = self.env['patient'].browse(patient_id)
        patient.write({
            'examination_date': self.examination_date,
            'department_id': self.department_id.id,
            'doctor_id': self.doctor_id.id if self.doctor_id else False,
        })
        return {'type': 'ir.actions.act_window_close'}
