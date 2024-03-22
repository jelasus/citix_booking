from email.policy import default
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

DEFAULT_BOOKING = {
    "guide": "HC002",
    "created_at": "2013-10-21",
    "reservation_date": "2013-10-21",
    "no_adults": 1,
    "no_children": 2,
    "no_babies": 3,
    "price_without_discounts": 3300.0,
    "gross_subtotal": 17000.0,
    "total_addons": 6000.0,
    "total_discounts": 7000.0,
    "total_coupons": 2.0,
    "subtotal": 2000.0,
    "total": 2200.0
}

DEFAULT_CHECK_IN_COMPANIONS = [
{
    "id": "C0001",
    "full_name": "Pedro Salinas Paria",
    "document_type": "Cédula de ciudadania",
    "document_number": "44345122",
    "phone_number": "987654321",
    "emergency_phone_number": "999666777",
    "person_type": "Adult",
    "gender": "Man"
},
{
    "id": "C0002",
    "full_name": "Jorge Luis Segura",
    "document_type": "Cédula de ciudadania",
    "document_number": "78782311",
    "phone_number": "987678352",
    "emergency_phone_number": "999666777",
    "person_type": "Children",
    "gender": "Man"
},
{
    "id": "C0003",
    "full_name": "Alfredo Julio Avendaño",
    "document_type": "Cédula de ciudadania",
    "document_number": "67440121",
    "phone_number": "984275123",
    "emergency_phone_number": "999666777",
    "person_type": "Baby",
    "gender": "Man"
}]

DEFAULT_REVIEW = {
    "stars": "4",
    "review": "Todo dispuesto para una feliz experiencia gastronómica. Sin teatro, sin fuegos artificiales, con gran profesionalidad. Cocina llena de matices para repasar la historia de esta casa desde sus inicios hasta la actualidad. Excelente servicio desde la llegada hasta la despedida. ",
    "created_at": "2013-10-21"
}

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
    booking = fields.Json(default=DEFAULT_BOOKING)
    review = fields.Json(default=DEFAULT_CHECK_IN_COMPANIONS)
    check_in_companions = fields.Json(default=DEFAULT_REVIEW)
