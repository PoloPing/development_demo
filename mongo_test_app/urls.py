from mongo_test_app.views import EntryViewSet
from development_demo.drf_routers import SharedAPIRootRouter

router = SharedAPIRootRouter()
router.register('entry', EntryViewSet, base_name='entry')
