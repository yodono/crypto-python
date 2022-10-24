from src import keys, symmetric, server, controller, router, encrypt_wl

if __name__ == "__main__":
    # Generate keys
    keys.generate_keys() # public key
    symmetric.generate_key() # symmetric key
    
    # Load keys
    private_key, public_key = keys.load_keys()
    symmetric_key = symmetric.load_key()

    # Encrypt whitelist
    encrypt_wl.encrypt(symmetric_key)

    # Initialize entities
    _server = server.local_server_factory(public_key, private_key, symmetric_key)
    _controller = controller.Controller(_server)

    # Define routes
    _router = router.Router()

    _router.get("/public_key", _controller.public_key)
    _router.post("/auth", _controller.auth)

    # Start server
    _server.run(_router)
