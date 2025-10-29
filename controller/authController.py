# Digita código
# import view.counterClick as cc

loginDb = 'user'
passwordDb = 'user'


class AuthController:

    def authenticate(self, login, password):
        try:
            if(login == loginDb and password == passwordDb):
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
            
# if __name__ == "__main__":
#     auth = AuthController()
    
