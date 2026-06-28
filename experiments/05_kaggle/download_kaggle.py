import builtins

original_open = builtins.open

def utf8_open(*args, **kwargs):
    # Only force utf-8 if opening for text mode (which is default if 'b' is not in mode)
    mode = args[1] if len(args) > 1 else kwargs.get('mode', 'r')
    if 'b' not in mode and 'encoding' not in kwargs:
        kwargs['encoding'] = 'utf-8'
    return original_open(*args, **kwargs)

builtins.open = utf8_open

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.kernels_output("aparajeetshadangi/cei-mbe-cifar10-grid", path=".")
