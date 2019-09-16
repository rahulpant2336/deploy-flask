from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
   name = TextField("",validators=[DataRequired()], render_kw={"placeholder": "Enter Your Name"})
   email = TextField("",validators=[DataRequired()], render_kw={"placeholder": "Enter Your Email"})
   subject = TextField("",validators=[DataRequired()], render_kw={"placeholder": "Subject"})
   message = TextAreaField("",validators=[DataRequired()], render_kw={"placeholder": "Message"})
   recaptcha = RecaptchaField()

   submit = SubmitField("Submit")
