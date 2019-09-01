# -*- coding: utf-8 -*-
from odoo import http

# class Practicasfct(http.Controller):
#     @http.route('/practicasfct/practicasfct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practicasfct/practicasfct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practicasfct.listing', {
#             'root': '/practicasfct/practicasfct',
#             'objects': http.request.env['practicasfct.practicasfct'].search([]),
#         })

#     @http.route('/practicasfct/practicasfct/objects/<model("practicasfct.practicasfct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practicasfct.object', {
#             'object': obj
#         })