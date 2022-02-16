# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import xlwt
from odoo.exceptions import Warning, ValidationError
import datetime
from odoo import tools
import math
from io import StringIO
import io
import base64



class Sale(models.Model):
	_inherit='sale.order'


	name2=fields.Char()

	
	
