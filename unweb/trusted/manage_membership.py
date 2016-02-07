from opencore.listen.browser.view import NuiManageMembersView
from Products.CMFCore.utils import getToolByName
from Products.listen.config import MEMBERSHIP_ALLOWED, MEMBERSHIP_DENIED
from Acquisition import aq_inner
from unweb.trusted import permissions

class ManageMembersView(NuiManageMembersView):

    def __call__(self):
        if self.request.get('subscribe'):
            self.subscribe_members()
        else:
            return NuiManageMembersView.__call__(self)

    def can_subscribe_others(self):
	"""
        returns true if the current user has the SubscribeOthers permission
        that allows adding new mailing list members directly
        without having them to confirm their membership after inviting them
        """
        mstool = getToolByName(self.context, 'portal_membership')
        return mstool.checkPermission('unweb.trusted: Subscribe others', self.context)


    def _add(self, user, subscribed, invite=True):
        request = {'action': 'add_allowed_sender', 'email': user}
        policy_result = self.policy.enforce(request)
        if policy_result == MEMBERSHIP_ALLOWED:
            self.mem_list.add_allowed_sender(user)
        elif policy_result == MEMBERSHIP_DENIED:
            return False

        if subscribed:
            request = {'action': 'subscribe', 'email': user}
            if (not invite and self.can_subscribe_others()) or self.policy.enforce(request) == MEMBERSHIP_ALLOWED:
                self.mem_list.subscribe(user)
        return True

    def subscribe_members(self):
        form = self.request.form
        CRLF = '\r\n'
        subscribed = True

        # results for PSMs
        added = []
        errors = []

        to_add = form.get('add_email', None).strip()

        if to_add and self.can_subscribe_others():
            # split on commas and newlines
            to_add = [ i.strip() for i in to_add.split(',') if i.strip() ]
            to_add = sum([ [ i.strip() for i in i.split(CRLF) if i.strip() ] for i in to_add ], [])

            for _to_add in to_add:
                if self._add(_to_add, subscribed, invite=False):
                    added.append(_to_add)
                else:
                    errors.append(_to_add)

        if added or errors:
            context = aq_inner(self.context)
            plone_utils = getToolByName(context, 'plone_utils')

            if errors:
                plone_utils.addPortalMessage('Bad user or email address: %s' % ', '.join(errors))

            if added:
                plone_utils.addPortalMessage('Added: %s' % ', '.join(added))
       
        self.request.response.redirect(self.context.absolute_url()+'/manage_membership')
