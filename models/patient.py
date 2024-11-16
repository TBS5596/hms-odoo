import logging

from dateutil.relativedelta import relativedelta
from datetime import datetime

from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class Patient(models.Model):
    _name = "patient.patient"
    _inherit = ['mail.thread']
    _description = "Patient"

    name = fields.Char(string="Name", tracking=True)
    first_name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name", required=True)
    dob = fields.Date(string="Date of Birth", required=True, tracking=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('female','Female'),('male','Male')], string="Gender", required=True)
    id_type = fields.Selection([('drivers license','Drivers License'),('passport','Passport'),('nrc','NRC')], string="ID Type", tracking=True)
    id_number = fields.Char(string="ID Number", tracking=True)

    ####################################### ON CHANGE FUNCTIONS ##########################################

    @api.onchange('first_name', 'last_name')
    def _set_name(self):
        self.name = f'{self.first_name} {self.last_name}'

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        self.name = f'{self.first_name} {self.last_name}'

    @api.onchange('dob')
    def _set_age(self):
        current_date = datetime.now()
        difference = relativedelta(current_date, self.dob)
        self.age = difference.years