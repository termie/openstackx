from openstackx.api import base


class RoleRef(base.Resource):
    pass

class RoleRefManager(base.ManagerWithFind):
    resource_class = RoleRef

    def get_for_user(self, user_id):
        return self._get("/users/%s/roleRefs" % user_id, "roleRefs")

    def add_for_tenant_user(self, tenant_id, user_id, role_id):
        params = {"roleRef": {"tenantId": tenant_id, "roleId": role_id}}
        return self._create("/users/%s/roleRefs" % user_id, params, "roleRef")

    def delete_for_tenant_user(self, tenant_id, user_id, role_id):

        role_refs = self.get_for_user(user_id)

        for role_ref in role_refs.values:
            if role_ref['roleId'] == role_id:
                return self._delete("/users/%s/roleRefs/%s" % (user_id, role_ref['id']))
