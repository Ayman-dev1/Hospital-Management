from odoo import models, fields
from odoo.exceptions import UserError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'


    patient_id = fields.Many2one('patient', string='Patient', required=True)

    def action_confirm(self):
        for order in self:
            if order.patient_id and order.patient_id.state != 'examination':
                raise UserError('The patient must be in the Examination state to confirm the sale order.')

            if order.patient_id:
                order.patient_id.state = 'done'

        return super(SaleOrderInherit, self).action_confirm()
