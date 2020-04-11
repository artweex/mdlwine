export default ({ $axios, redirect }) ->
	$axios.onRequest (config) ->
		console.log('Making request to ' + config.url)


	$axios.onError (error) ->
		# console.log(error)
		code = parseInt(error.response && error.response.status)
		console.log(error.errno)
		# if code is 400
		# 	redirect('/400')
