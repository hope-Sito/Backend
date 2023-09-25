from .oauth2 import Role, RoleChecker

# доступно только админу
admin: RoleChecker = RoleChecker(Role.ADMIN)
# доступно админам и членам
member: RoleChecker = RoleChecker([Role.MEMBER, Role.GUEST])
# доступно админам, членам и гостям
guest: RoleChecker = RoleChecker([Role.GUEST, Role.MEMBER, Role.MEMBER])
