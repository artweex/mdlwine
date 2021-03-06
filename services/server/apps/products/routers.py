from rest_framework import routers
from .views import Products


from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class ReadOnlyRouter(SimpleRouter):
	"""
	A router for read-only APIs, which doesn't use trailing slashes.
	"""
	routes = [
		Route(
			url=r'^{prefix}$',
			mapping={'get': 'list'},
			name='{basename}-list',
			detail=False,
			initkwargs={'suffix': 'List'}
		),
		Route(
			url=r'^{prefix}/{lookup}$',
			mapping={'get': 'retrieve'},
			name='{basename}-detail',
			detail=True,
			initkwargs={'suffix': 'Detail'}
		),
		# DynamicRoute(
		#     url=r'^{prefix}/{lookup}/{url_path}$',
		#     name='{basename}-{url_name}',
		#     detail=True,
		#     initkwargs={}
		# )
	]


router = ReadOnlyRouter()

router.register(r'products', Products)