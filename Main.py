from Classes.Networking.ServerConnection import ServerConnection
from Classes.Utilities.Preloader import Preloader

Preloader.preloadAll()
ServerConnection(("0.0.0.0", 9339))