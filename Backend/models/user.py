import base64

class User:

    def __init__(self, firstName, lastName, email, username, password, adminOrNot):

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password
        self.adminOrNot = adminOrNot

    def __dict__(self):
        
        return {
            "First Name" : self.firstName,
            "Last Name" : self.lastName,
            "Email" : self.email,
            "Username" : self.username,
            "Password" : self.password,
            "Admin Status" : self.adminOrNot
        }

    def setAdmin(self, adminOrNot):
        self.adminOrNot = adminOrNot

    def setFirstName(self, fnameToSet):
        self.firstName = fnameToSet

    def setLastName(self, lnameToSet):
        self.lastName = lnameToSet

    def resetPassword(self, newPassword):
        self.password = newPassword

    def changeEmail(self, newEmail):
        self.email = newEmail

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def verifyPassword(self, passwordEnter):
        if passwordEnter != self.password:
            print("Password is incorrect, Try Again.")
        else:
            print("Password is Correct.")

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def isAdmin(self):
        if self.adminOrNot == True:
            return True
        else:
            return False

    def encodePassword(self, ePassword):
        encode_string = ePassword
        encode_string_bytes = encode_string.encode("ascii")
  
        base64_bytes = base64.b64encode(encode_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        return base64_string

    def decodePassword(self, dPassword):
        base64_string = dPassword
        base64_bytes = base64_string.encode("ascii")
  
        decode_string_bytes = base64.b64decode(base64_bytes)
        decode_string = decode_string_bytes.decode("ascii")
    
        return decode_string

