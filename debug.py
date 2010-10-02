

from dev_deployment import settings


def jab(text, toAccount, fromAccount, fromPass):
    
    # http://xmpppy.sourceforge.net/
    import xmpp
    
    jid = xmpp.protocol.JID(fromAccount)
    
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    if not con:
        raise Exception('Jabber: con=cl.connect()')
    
    auth = cl.auth(jid.getNode(), fromPass, resource=jid.getResource())
    if not con:
        raise Exception('Jabber: cl.auth')
    
    id = cl.send(xmpp.protocol.Message(toAccount, text))