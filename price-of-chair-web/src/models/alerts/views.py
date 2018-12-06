from flask import Blueprint

alert_bleuprint = Blueprint('alert', __name__)


@alert_bleuprint.route('/new', methods=["POST"])
def create_alert():
    pass

@alert_bleuprint.route('/deactivate(<string:alert_id>')
def deactivate_alert(alert_id):
    pass

@alert_bleuprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
    pass

@alert_bleuprint.route('/for_user/<string:user_id>')
def get_alerts_for_user():
    pass



