from odoo import models, fields

class res_partner(models.Model):
   _inherit = "res.partner"

   telegram_chat_id = fields.Integer("Telegram Chat ID")
   identifier = fields.Integer("Identificador")
