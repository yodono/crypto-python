import keys
import server
import controller
import router

keys.generate_keys()
private_key, public_key = keys.load_keys()

_server = server.local_server_factory(public_key, private_key)
_controller = controller.Controller(_server)
_router = router.Router()

_router.get("/public_key", _controller.public_key)
_router.post("/auth", _controller.auth)
# _router.post("auth", _controller.auth)

_server.run(_router)
