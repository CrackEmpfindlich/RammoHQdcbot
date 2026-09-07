class PermissionUtils:
    @staticmethod
    def check_permission(user, required_permission):
        return user.permissions >= required_permission
