import webapp2

form = """
<form method="post">
        What is your birthday?
        <br>
	    <label>
			Month
			<input type="text" name="month" value="%(month)s">
		</label>
		
		<label>
			Day
			<input type="text" name="day" value="%(day)s">
		</label>
		
		<label>
			Year
			<input type="text" name="year" value="%(year)s">
		</label>
		<div style="color: red">%(error)s</div>		
		<br>
        <br>
        <input type = "submit">
       
</form>
"""

def valid_month(month):
    return False
def valid_day(day):
    return True

def valid_year(year):
    return True
  
    
class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error, 
        "month": month, 
        "day":day, 
        "year":year})
    def get(self):
        self.write_form()
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        
        if not(month and day and year):
            self.write_form("Thats wrong", user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks! Thats valid")
        
    
        
   
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)      
     