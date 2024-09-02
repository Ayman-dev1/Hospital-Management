# -*- coding: utf-8 -*-
# from odoo import http


# class OdooHos(http.Controller):
#     @http.route('/odoo_hos/odoo_hos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_hos/odoo_hos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_hos.listing', {
#             'root': '/odoo_hos/odoo_hos',
#             'objects': http.request.env['odoo_hos.odoo_hos'].search([]),
#         })

#     @http.route('/odoo_hos/odoo_hos/objects/<model("odoo_hos.odoo_hos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_hos.object', {
#             'object': obj
#         })
