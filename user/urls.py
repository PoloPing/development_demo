from user.views import UserViewSet
from development_demo.drf_routers import SharedAPIRootRouter

router = SharedAPIRootRouter()
router.register('user', UserViewSet, base_name='user')
