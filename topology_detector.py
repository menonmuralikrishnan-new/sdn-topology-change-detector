from pox.core import core
import pox.openflow.libopenflow_01 as of

log=core.getLogger()

def _handle_ConnectionUp(event):
	log.info("Switch connected: %s", event.connection)

def _handle_ConnectionDown(event):
	log.info("Switch disconnected : %s",event.connection)

def _handle_PacketIn(event):
	packet=event.parsed
	log.info("Packet received from %s",event.connection)
def launch():
	log.info("Topology Change Detector Started")
	core.openflow.addListenerByName("ConnectionUp",_handle_ConnectionUp)
	core.openflow.addListenerByName("ConnectionDown",_handle_ConnectionDown)
	core.openflow.addListenerByName("PacketIn",_handle_PacketIn)

