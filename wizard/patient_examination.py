from odoo import models, fields, api


class PatientExamination(models.TransientModel):
    _name = 'patient.examination'
    _description = 'Examination Wizard'

    examination_date = fields.Date(string='Examination Date', required=True)
    department_id = fields.Many2one('department', string='Department', required=True)
    doctor_id = fields.Many2one('doctor', string='Doctor', required=True)
