/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart } from "@odoo/owl";

export class BookingWidget extends Component {
  setup() {
    this.orm = useService("orm");
    onWillStart(this.onWillStart);
  }

  async onWillStart() {
    var id = this.props.record.evalContext.id;
    if (!id) {
      id = 1; // action show example data
    }
    this.resBooking = await this.orm.searchRead(
      this.props.record.resModel,
      [["id", "=", id]],
      ["booking", "review", "check_in_companions"]
    );
  }

  getBookingField() {
    return JSON.parse(this.resBooking[0].booking);
  }

  getReviewField() {
    return JSON.parse(this.resBooking[0].review);
  }

  getCheckInCompanionsField() {
    return JSON.parse(this.resBooking[0].check_in_companions);
  }
}

BookingWidget.template = "citix_booking.Booking";

export const bookingWidget = {
  component: BookingWidget,
};

registry.category("view_widgets").add("booking", bookingWidget);
