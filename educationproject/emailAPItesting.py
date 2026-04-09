def sendMail(email, password, subject="", html="", purpose_url=""):

    html = """<html>
                <head></head>
                <body>
                    <h1>Welcome to Activity School</h1>
                    <p>You have successfully registered , please click on the link below to verify your account</p>
                    <h2>Username : """+email+"""</h2>
                    <h2>Password : """+str(password)+"""</h2>
                    <br>
                    <a href='http://localhost:8000/verify?vemail="""+email+"""' >Click here to verify account</a>		
                    <a href='"""+purpose_url+"""' >Click here to verify account</a>		
                </body>
            </html>
        """
    return html
