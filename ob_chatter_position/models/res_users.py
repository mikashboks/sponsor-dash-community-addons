# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    chatter_position = fields.Selection(
        [("normal", "Normal"), ("sided", "Sided")],
        default="sided",
    )

    #  Override so that the user can change the chatter_position field

    def __init__(self, pool, cr):
        """ Override of init to allow user to set its chatter position. """
        init_res = super(ResUsers, self).__init__(pool, cr)

        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['chatter_position'])

        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['chatter_position'])
        return init_res
