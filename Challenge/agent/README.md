# srvcompliance

Agente
El agente es un programa en Python que recolecta la siguiente información del sistema operativo:

Información sobre el procesador.
Listado de procesos corriendo.
Usuarios con una sesión abierta en el sistema.
Nombre del sistema operativo.
Versión del sistema operativo.

PARA EL AGENTE 
### Crear al ambiente
python3 -m venv /home/admin/agent/srvcompliance/srvc-env
### Activar el ambiente
source /home/admin/agent/srvcompliance/srvc-env/bin/activate
###Instalar requirements
pip install -r requirements.txt
### Ejecucion 
python3 agent.py
