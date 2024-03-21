from odoo import fields, models

TYPE_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('finished', 'Finished'),
]
DEFAULT_CHOICE = 'pending'
TYPES = [
    ('restaurant', 'Restaurant'),
    ('place', 'Place'),
    ('travel', 'Travel'),
    ('other', 'Other'),
]
DEFAULT_TYPE = 'other'


class Booking(models.Model):

    _name = 'booking'
    _inherit = ['image.mixin']

    # required fields

    # module info
    choice = fields.Selection(
        selection=TYPE_CHOICES,
        required=True,
        default=DEFAULT_CHOICE,
    )

    # service info
    name = fields.Char('Title name', required=True)
    detailed_type = fields.Selection(
        selection=TYPES,
        required=False,
        default=DEFAULT_TYPE,
    )

    # booking info
    booking = fields.Json()
    review = fields.Json()
    check_in_companions = fields.Json()
