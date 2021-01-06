import casbin

e = casbin.Enforcer("rbac_model.conf", "rbac_policy.csv")
sub = "alice"
obj = "data1"
act = "read"

if e.enforce(sub, obj, act):
    print("permit alice to read data1")
else:
    print("deny the request, show an error")

roles = e.get_roles_for_user("alice")
print(roles)