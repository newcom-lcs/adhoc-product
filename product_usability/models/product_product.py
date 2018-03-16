# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    active = fields.Boolean(track_visibility='onchange')