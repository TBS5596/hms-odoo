from odoo import fields, models, api

class Appointment(models.Model):
    _name = "appointment.appointment"
    _inherit = ['mail.thread']
    _description = "Appointment"
    _rec_name = "patient_id"

    reference = fields.Char(string="Reference", default="New")
    appointment_date = fields.Date(string="Date", required=True, tracking=True)
    patient_id = fields.Many2one('patient.patient', string="Patient", required=True, tracking=True)
    purpose = fields.Text(string="Purpose", required=True)

    @api.model_create_multi
    def create(self, val_list):
        for val in val_list:
            if not val.get('reference') or val['reference'] == "New":
                val['reference'] = self.env['ir.sequence'].next_by_code('appointment.appointment')
        return super().create(val_list)