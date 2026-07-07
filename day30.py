def lookup_profile():
    # Hardcoded dictionary matching usernames to ID numbers
    user_database = {"indrajit": 101, "prajit": 102, "admin": 999}
    
    # Hardcoded list of active servers
    active_servers = ["Server_Alpha", "Server_Beta"]

    try:
        # 1. Test Key Error
        username = input("Enter username to look up: ").lower()
        user_id = user_database[username] # Raises KeyError if name isn't there
        print(f"✅ User found! ID: {user_id}")
        
        # 2. Test Index Error
        server_choice = int(input("Connect to Server Index (0 or 1): "))
        server_name = active_servers[server_choice] # Raises IndexError if user enters 2 or higher
        print(f"🚀 Successfully connected to {server_name}")
        
    except KeyError:
        print("❌ System Error: That username does not exist in our system database.")
    except IndexError:
        print("❌ System Error: Invalid server location selected. Out of bounds.")
    except ValueError:
        print("❌ System Error: Server index must be a numeric integer value.")

# Run the project
lookup_profile()