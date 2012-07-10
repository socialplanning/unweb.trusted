from Products.CMFCore.permissions import setDefaultRoles

SubscribeOthers = "unweb.trusted: Subscribe others"
setDefaultRoles(SubscribeOthers, ('Manager','Trusted List Admin'))

