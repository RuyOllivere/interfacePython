# Digita código
# import view.counterClick as cc

loginDb = 'user'
passwordDb = 'password'


class AuthController:

    def authenticate(self, login, password):
        try:
            if(login == loginDb and password == passwordDb):
                return print("Authentication made!")
            else:
                return print("Wrong login or password, a**hole!")

        except Exception as e:
            print(f"Error: {e}")
            
# if __name__ == "__main__":
#     auth = AuthController()
    
