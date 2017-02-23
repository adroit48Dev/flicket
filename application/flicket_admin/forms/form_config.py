
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange

form_class_button = {'class': 'btn btn-primary'}


class ConfigForm(FlaskForm):

    mail_server = StringField('mail_server', validators=[])
    mail_port = IntegerField('mail_port', validators=[NumberRange(min=1, max=65535)])
    mail_use_tls = BooleanField('mail_use_tls', validators=[])
    mail_use_ssl = BooleanField('mail_use_ssl', validators=[])
    mail_debug = BooleanField('mail_debug', validators=[])
    mail_username = StringField('mail_username', validators=[])
    mail_password = StringField('mail_password', validators=[])
    mail_default_sender = StringField('mail_default_sender', validators=[])
    mail_max_emails = IntegerField('mail_max_emails', validators=[])
    mail_suppress_send = BooleanField('mail_suppress_send', validators=[])
    mail_ascii_attachments = BooleanField('mail_ascii_attachments', validators=[])

    posts_per_page = IntegerField('posts_per_page', validators=[DataRequired(), NumberRange(min=10, max=100)])
    allowed_extensions = StringField('allowed_extensions', validators=[DataRequired()])
    ticket_upload_folder = StringField('ticket_upload_folder', validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw=form_class_button, validators=[DataRequired()])
