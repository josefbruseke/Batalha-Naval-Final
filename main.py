import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from controle.controlador_sistema import ControladorSistema

if __name__ == "__main__":
    ControladorSistema().inicializa_sistema()