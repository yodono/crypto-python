import keys
import symmetric
import server
import controller
import router
import encrypt_wl

keys.generate_keys()
private_key, public_key = keys.load_keys()

symmetric.generate_key()
symmetric_key = symmetric.load_key()
encrypt_wl.encrypt(symmetric_key)

_server = server.local_server_factory(public_key, private_key, symmetric_key)
_controller = controller.Controller(_server)
_router = router.Router()

_router.get("/public_key", _controller.public_key)
_router.post("/auth", _controller.auth)

_server.run(_router)
