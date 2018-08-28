# -*- coding: utf-8 -*-
from odoo import http
import xmlrpc, xmlrpc.client
import json

class Restfulapi(http.Controller):
    
    @http.route('/restfulapi/login', auth='none', type="http")
    def login(self, **kw):
        xmlrpclib = xmlrpc.client
        url, db, username, password = 'http://localhost:8069', http.request.env.cr.dbname, kw.get('username'), kw.get('password')
        common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
        try:
            uid = common.authenticate(db, username, password, {})
            return json.dumps({'user_id':uid})
        except:
            return json.dumps({'Error':'Invalid Request'})
     
    @http.route('/restfulapi/get-products', auth='none', type="http")
    def get_products(self, **kw):
        xmlrpclib = xmlrpc.client
        url, db, username, password = 'http://localhost:8069', http.request.env.cr.dbname, kw.get('username'), kw.get('password')
        models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
        common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
        try:
            uid = common.authenticate(db, username, password, {})
            res = models.execute_kw(db, uid, password, 'product.product', 'search_read', [], {})
            return json.dumps({'products':res})
        except:
            return json.dumps({'Error':'Invalid Request'})
            